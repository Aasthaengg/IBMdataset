n = int(input())
al = list(map(int, input().split()))
al.sort(reverse=True)
ans = 0
for i in range(n):
    ans += al[2*i+1]
print(ans)