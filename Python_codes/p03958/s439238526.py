k,t = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = A[0]-1
for a in A[1:]:
    ans -= a
    if ans < 0:
        ans = 0
        break
print(ans)