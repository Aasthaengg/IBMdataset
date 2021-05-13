n = int(input())
l = list(map(int,input().split()))

a=[]
b={}
ans=0

for i in range(n):
    a.append(i+l[i])
    b[i-l[i]] = b.get(i-l[i],0) + 1

for av in a:
    ans = ans + b.get(av,0)

print(ans)