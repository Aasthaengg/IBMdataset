A, B, K = map(int, input().split())

ans1 = [i for i in range(A, A + K) if A <= i and i <= B]
ans2 = [i for i in range(B, B - K, -1) if A <= i and i <= B]

ans = ans1 + ans2
ans = list(set(ans))
ans.sort()
for ans in ans:
    print(ans)