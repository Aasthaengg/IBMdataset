n=int(input())
c=0
for i in list(map(int,input().split()))[::2]:
  c+=i%2
print(c)