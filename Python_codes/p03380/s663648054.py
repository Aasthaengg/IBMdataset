n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

tmp = a[0]//2
s = 10**18
num = 0
for i in range(1, n):
    if(abs(tmp-a[i]) < s):
        s = abs(tmp-a[i])
        num = a[i]

print(a[0], num)