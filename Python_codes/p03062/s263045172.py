n = int(input())
aas = list(map(int, input().split()))
cnt = 0
res = 0
mini = float('inf')
for i in aas:
    if i < 0:
        cnt += 1
    res += abs(i)
    mini = min(mini, abs(i))
if cnt%2 == 0:
    print(res)
    exit()
print(res - mini*2)