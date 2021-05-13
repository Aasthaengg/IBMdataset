N=int(input())
l= list(map(int,input().split()))
l.sort()
S=0
ans=0
for i in range(N-1):
   S+=l[i]
   if S*2<l[i+1]:
      ans=i+1
print(N-ans)