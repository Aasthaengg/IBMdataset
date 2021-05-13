n = int(input())
a = list(map(int,input().split()))
ans = 3 ** n
o = 1
for i in range(n):
    if a[i] % 2 == 0:
        o *= 2
    else:
        o *= 1
print(ans - o)