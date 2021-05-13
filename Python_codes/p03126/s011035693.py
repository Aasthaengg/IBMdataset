n,m = map(int,input().split())
s = set(list(map(int,input().split()))[1:])
for i in range(n-1):
 s &= set(list(map(int,input().split()))[1:])
print(len(s))