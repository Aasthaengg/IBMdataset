n = int(input())
al = list(map(int,input().split()))

ans = 3 ** n
tmp = 1
for a in al:
    if a % 2 == 0:
        tmp *= 2

print(ans-tmp)