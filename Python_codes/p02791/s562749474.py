n = int(input())
li = list(map(int,input().split()))
a = 200000
c = 0
for i in range(n):
    if li[i] <= a:
        c += 1
        a = li[i]
print(c)