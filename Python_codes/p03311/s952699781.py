N = int(input())
*A, = map(int, input().split())
l = [j-i for i, j in enumerate(A, start=1)]
l.sort()

b = l[N//2]
ans = 0
for i in l:
    ans += abs(i-b)
print(ans)
