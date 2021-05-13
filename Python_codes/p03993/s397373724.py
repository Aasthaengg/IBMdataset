n = int(input())
al = list(map(int, input().split()))
cnt = 0
for i in range(n):
    tmp = al[i]
    if al[tmp-1] == i+1:
        cnt += 1
    else:
        pass
print(cnt//2)