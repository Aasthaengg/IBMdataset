N = int(input())
A = list(map(int, input().split()))
Cnt = [0] * (N+1)
for a in A:
    Cnt[a] += 1
ans0 = 0
for c in Cnt:
    ans0 += c * (c-1) // 2
Ans = [ans0 - Cnt[a] + 1 for a in A]
print("\n".join(map(str, Ans)))
