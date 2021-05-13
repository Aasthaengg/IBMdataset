N = int(input())
d = [int(input()) for i in range(N)]

x = sorted(d, reverse=True)

ans = 1
for i in range(N-1):
    if x[i] - x[i+1] >0:
        ans += 1
    else:
        continue


print(ans)
