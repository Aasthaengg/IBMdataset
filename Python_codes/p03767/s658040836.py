N = int(input())
a = list(map(int,input().split()))

a.sort()

ans = a[N:]
ans = ans[::2]
print(sum(ans))