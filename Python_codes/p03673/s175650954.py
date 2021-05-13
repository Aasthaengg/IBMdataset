n = int(input())
a = list(map(int, input().split()))
ans1 = list(range(1, n+1, 2))
ans2 = list(range(2, n+1, 2))
if n % 2 == 0:
    ans2.reverse()
    ans = ans2 + ans1
else:
    ans1.reverse()
    ans = ans1 + ans2
for i in ans:
    print(a[i-1])
