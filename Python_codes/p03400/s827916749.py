ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
d,x=nm()

cnt=0
for i in range(n):
  a = ni()
  for j in range(1,d+1,a):
    cnt+=1

print(cnt+x)
