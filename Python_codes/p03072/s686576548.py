N = int(input())
H = list(map(int, input().split()))

ans = 1

for i in range(1,N):
    for j in range(i):
        if H[j] <= H[i]:
            if j == i-1:
                ans += 1
            continue
        else:
            break


print(ans)
