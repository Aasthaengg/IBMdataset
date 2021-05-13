n = int(input())
p = list(map(int, input().split()))

cnt = 0
for i in range(n-2):
    test = sorted(p[i:i+3])
    if test[1] == p[i+1]:
        cnt += 1

print(cnt)
