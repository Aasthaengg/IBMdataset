import bisect
n = int(input())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
cl = list(map(int, input().split()))
al.sort()
bl.sort()
cl.sort()
ans = 0
tmp1 = [n]*n
tmp2 = [n]*n
for i in range(n):
    j = bisect.bisect_left(al, bl[i])
    tmp1[i] = j
for i in range(n):
    j = bisect.bisect_right(cl, bl[i])
    tmp2[i] = n-j
for i in range(n):
    ans += tmp1[i]*tmp2[i]
print(ans)
