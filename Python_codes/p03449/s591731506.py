N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0

for i in range(N):
    ans_ = sum(A[:i + 1])
    ans_ += sum(B[i:])
    ans = max(ans, ans_)

print(ans)
