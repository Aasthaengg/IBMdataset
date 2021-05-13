def divi(n):
  ans = 0
  a2 = 0 
  while n >= 2 ** a2:
    ans = 2 ** a2
    a2 += 1
  return ans

    
N = int(input())

answ = divi(N)
print(answ)