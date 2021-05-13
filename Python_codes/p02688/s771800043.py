from sys import stdin,stdout
# n=int(stdin.readline())
n,k=list(map(int,stdin.readline().split()))
s=set()
for _ in range(k):
    x=input()
    for v in map(int,stdin.readline().split()):
        s.add(v)
ans=0
for i in range(1,n+1):
    if i not in s:ans+=1
print(ans)