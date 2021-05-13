n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

ans = 0
for i in range(n):
    tmp = sum(al[0:i+1]) + sum(bl[i:])
    if ans < tmp:
        ans = tmp
print(ans)