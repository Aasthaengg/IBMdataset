n = int(input())
a = list(map(int,input().split()))
av = sum(a)/len(a)

ans = 0
j = 101
for i in range(n):
    tmp = abs(a[i]-av)
    if j > tmp:
        j = tmp
        ans = i

print(ans)