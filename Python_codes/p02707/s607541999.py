N = int(input())
A = list(map(int, input().split()))
Ans = [0] * (N+1)
for a in A:
    Ans[a] += 1
print("\n".join(map(str, Ans[1:])))
