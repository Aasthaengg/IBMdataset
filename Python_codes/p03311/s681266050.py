n = int(input())
a = list(map(int, input().split()))
aa = []
for i, j in enumerate(a):
    aa.append(j-i-1)
aa.sort()
b = aa[n//2]
ans = 0
for i in aa:
    ans += abs(i-b)
print(ans)