n = int(input())
lis =[0] + list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    if lis[lis[i]] == i:
        cnt += 1

print(cnt//2)