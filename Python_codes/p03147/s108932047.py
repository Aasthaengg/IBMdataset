N = int(input())
H = list(map(int, input().split()))


def down(H, l, r):
    for i in range(l, r):
        H[i] -= 1


s = 0
for h in range(100):
    # LとRを求める
    l = 0
    while l < N:
        if H[l]:
            for j in range(l+1, N):
                if H[j] == 0:
                    r = j
                    break
            else:
                r = N
            down(H, l, r)
            s += 1
            l = r+1
        else:
            l += 1
print(s)
