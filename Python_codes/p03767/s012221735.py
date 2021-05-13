N = int(input())
la = list(map(int, input().split()))

la = sorted(la, reverse=True)
# print(la)

ans = 0
for i in range(1, 2*N, 2):
    ans += la[i]
    la[i]

print(ans)