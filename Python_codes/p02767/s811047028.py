n = int(input())
x = list(map(int, input().split()))
ans = []
for i in range(1, 101):
    tmp = 0
    for j in range(n):
        tmp += pow(x[j]-i, 2)
    ans.append(tmp)
print(min(ans))