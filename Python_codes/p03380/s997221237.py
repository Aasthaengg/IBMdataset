n = int(input())
a = list(map(int, input().split()))

ansn = max(a)
b = list(map(lambda x: abs(x-ansn/2), a))

minu = 10**9+1
ind = 0

for i in range(n):
  if b[i] <= minu:
    minu = b[i]
    ind = i
    
print(str(ansn)+" "+str(a[ind]))