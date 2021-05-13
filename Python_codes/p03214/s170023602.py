n=int(input())
a=list(map(int,input().split()))
v=sum(a)/n
d=1000
t=0
for i in range(n):
  if abs(v-a[i])<d:
    d=abs(v-a[i])
    t=i
print(t)