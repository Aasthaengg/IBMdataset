N = int(input())
C = input()

tmp = 0
for i in range(N):
    if C[i] == "R":
        tmp += 1

ans = 0
for i in range(tmp):
    if C[i] == "W":
        ans += 1
print(ans)