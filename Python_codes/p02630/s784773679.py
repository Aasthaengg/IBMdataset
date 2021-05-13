N = int(input())
A = list(map(int, input().split()))
Ad, ans = {}, sum(A)
for a in A:
    Ad[a] = Ad.get(a, 0) + 1

Q = int(input())
for _ in range(Q):
    B, C = map(int, input().split())
    ans += (C - B) * Ad.get(B, 0)
    Ad[B], Ad[C] = 0, Ad.get(B, 0) + Ad.get(C, 0)
    print(ans)
