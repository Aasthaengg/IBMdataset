n=int(input())
a=[0]*-~n;b=[0]*-~n
mx=-1
mi=-1
for i in range(n):
  a[i], b[i] = map(int,input().split())
  if a[i] > mx:
    mx = a[i]; mi = i

print(mx+b[mi])