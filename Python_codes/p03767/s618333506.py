n = int(input())
a = list(map(int,input().split()))
a = sorted(a)[::-1]
ans = sum(a[1:2*n:2])
print(ans)