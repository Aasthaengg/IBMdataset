def is_prime(q):
    if q < 2 or q&1 == 0: return False
    return pow(5, q-1, q)*pow(7, q-1, q) == 1
  
def main():
  mod = 10**9+7
  n = int(input())
  ans = 1
  if n == 1:
    print(1)
    exit()
  
  b = [2]
  for i in range(2,min(n+1,998)):
    if i == 5 or i == 7:
      b.append(i)
    if i == 561:
      continue
    if is_prime(i):
      b.append(i)
      
  for i in b:
    p = i
    cnt = 1
    chk = 1
    for j in range(10):
      chk += n//p
      if p > n:
        ans *= chk
        ans %= mod
        chk = 1
        break
      p *= i
      
  print(ans)

if __name__ == '__main__':
    main()