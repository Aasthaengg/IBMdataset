## B - 仲良しうさぎ
N = int(input())
A = [0] + list(map(int, input().split()))
ans = 0
for i in range(1,N+1):
    if A[A[i]] == i:
        ans += 1
print(ans//2)