N = int(input())
F = []
P = []

for i in range(N):
    Fi = list(map(int, input().split()))
    F.append(Fi)

for i in range(N):
    Pi = list(map(int, input().split()))
    P.append(Pi)

ans = -10 ** 18

# print(F)
for i in range(1, 2**10):
    kaburi_list = []
    tmp = 0
    for tenpo in range(N):
        kaburi = 0
        for j in range(10):
            if i >> j & F[tenpo][-(j+1)] == 1:
                kaburi += 1
        kaburi_list.append(kaburi)
        tmp += P[tenpo][kaburi]
    ans = max(ans, tmp)

print(ans)
