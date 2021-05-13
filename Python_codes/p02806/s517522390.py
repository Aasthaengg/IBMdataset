n=int(input())
a=[(input().split()) for _ in range(n)]
x=input()
cnt='x'
for i in a:
  if cnt!='x':
    z=int(i[1])
    cnt+=z
  if i[0]==x:
    cnt=0
print(cnt)