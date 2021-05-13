N = int(input())
H = [int(i) for i in input().split()]

ans = 0
while sum(H) > 0:
    pre = 0
    for i in range(N):
        if pre > 0 and H[i] == 0:
            break
        if H[i] != 0:
            H[i] -= 1
            pre = H[i] + 1
    ans += 1

print(ans)