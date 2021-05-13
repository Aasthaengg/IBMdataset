n = int(input())
ab =[list(map(int,input().split())) for _ in range(n)]

ab.sort()
a = []
b =[]
for x in ab:
  a.append(x[0])
  b.append(x[1])
a.sort()
b.sort()

ca,cb =0,0
if n % 2 == 0:
  ca = (a[n//2-1] + a[n//2])/2
  cb = (b[n//2-1] + b[n//2])/2
  ans = int((cb-ca)//0.5+1)
else:
  ca = a[(n+1)//2-1]
  cb = b[(n+1)//2-1]
  ans = (cb-ca) +1

print(int(ans))