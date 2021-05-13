N=int(input())

ans = 0
tmp = 1
while tmp*2 <= N:
    ans += 1
    tmp *= 2
print(tmp)