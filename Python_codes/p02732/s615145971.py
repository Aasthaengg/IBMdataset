def nC2 (n):
    return n*(n-1)//2 

N = int(input())
A = tuple(map(int,input().split()))
cnt = [0]*200005
tot = 0
for i in A:
    cnt[i] += 1
for i in cnt:
    tot += nC2(i)
for i in range(N):
    ans = tot - nC2(cnt[A[i]]) + nC2(cnt[A[i]]-1)
    print(ans)