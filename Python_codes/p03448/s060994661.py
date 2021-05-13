ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a=ni()
b=ni()
c=ni()
x=ni()

cnt=0
for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      if 500*i+100*j+50*k==x:
        cnt+=1
print(cnt)
