n = int(input())
al = list(map(int, input().split()))

cnt = 0
for i in range(n):
    j = al[i]
    if al[j-1] == i + 1:
        cnt += 1

print(cnt//2)