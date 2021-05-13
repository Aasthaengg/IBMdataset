n=int(input())
a=list(map(int,input().split()))[::2]
c=0
for i in a:
  c+=(i%2)
print(c)