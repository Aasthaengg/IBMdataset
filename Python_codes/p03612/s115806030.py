n = int(input())
p = list(map(int,input().split()))
ans = 0
cou = 0
for i in range(n):
    if p[i] == i+1:
        cou += 1
    elif p[i] != i+1:
        ans += -(-cou//2)
        cou = 0

ans += -(-cou//2)
print(ans)