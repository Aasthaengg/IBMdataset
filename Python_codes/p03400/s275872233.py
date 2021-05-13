n=int(input())
d,x=map(int,input().split())
a=[int(input()) for _ in range(n)]
count=0
for i in a:
  day=1
  while day <= d:
    day+=i
    count+=1
print(count+x)