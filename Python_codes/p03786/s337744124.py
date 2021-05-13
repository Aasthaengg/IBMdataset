import itertools
n=int(input())
a= list(map(int, input().split()))
a.sort()
aa = list(itertools.accumulate(a))
ans=1

for i in range(n-1):
    if aa[n-2-i]*2>=a[n-1-i]:
        ans+=1
    else:
        break

print(ans)