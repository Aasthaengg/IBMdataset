import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
B_ans = [0]*N
A.sort()
B.sort()
C.sort()
ans = 0

for i, b in enumerate(B):
    bi = bisect.bisect_left(A, b)
    B_ans[i] = B_ans[i-1] + bi
for j, c in enumerate(C):
    ci = bisect.bisect_left(B, c)
    if ci == 0:
        continue

    ans += B_ans[ci-1]
print(ans)
