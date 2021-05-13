from collections import Counter
N = int(input())
S = ["".join(sorted(input())) for i in range(N)]
ans = 0
for i in Counter(S).values():
    ans += i*(i-1)//2
print(ans)