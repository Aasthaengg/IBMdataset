n = int(input())
h = list(map(int, input().split()))

ans = 0
step = 0
i = 0
while i < len(h)-1:
    if h[i] >= h[i+1]:
        step +=1
        ans = max(ans, step)
    else:
        step = 0
    i += 1

print(ans)