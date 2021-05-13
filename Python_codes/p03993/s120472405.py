n = int(input())
a = list(map(int,input().split()))
c = 0
a = [0] + a
for i in range(n):
    if i == a[a[i]]:
        c += 1
else:
    print(c//2)