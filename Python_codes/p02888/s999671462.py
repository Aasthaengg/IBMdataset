import bisect
N = int(input())
ls = list(map(int,input().split()))
ls.sort()
ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        ls1 = ls[j+1:]
        ans += bisect.bisect_left(ls1,ls[j]+ls[i])-bisect.bisect(ls1,ls[j]-ls[i])
print(ans)