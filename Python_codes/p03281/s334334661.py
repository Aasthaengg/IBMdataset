n = int(input())

cnt = 0
def primes(num):
  arr = []
  for i in range(1,int(num*(0.5))+1):
    if num%i == 0 and i not in arr:
      arr.append(i)
      if num//i not in arr:
        arr.append(num//i)
  return arr
      
for i in range(1,n+1,2):
  if len(primes(i))==8:
    cnt += 1
print(cnt)