n = int(input())
a = sorted(list(map(int,input().split())))
b = a[:]
for i in range(1,n):
  b[i] = b[i]+b[i-1]

a = a[::-1]
b = b[::-1]

cnt=1
for i in range(1,n):
  if b[i]*2>=a[i-1]:
    cnt+=1
  else:
    break
print(cnt)