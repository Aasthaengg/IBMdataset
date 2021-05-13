n = int(input())
p = list(map(int, input().split()))

tmpmin = float('inf')
cnt = 0
for pi in p:
    if tmpmin >= pi:
        cnt += 1
        tmpmin = pi

print(cnt)
