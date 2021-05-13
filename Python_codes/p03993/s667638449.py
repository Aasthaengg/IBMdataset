N = int(input())
a_li = list(map(int, input().split()))
ans = 0
chk = []
for i in range(N):
    if i + 1 == a_li[a_li[i] - 1] :
        ans += 1
print(int(ans / 2))
