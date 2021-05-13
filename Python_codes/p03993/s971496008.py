n = int(input())
a = [int(x)-1 for x in input().split()]

ans = 0
for i,x in enumerate(a):
    if a[x] == i and a[i] == x:
        ans += 1

print(ans//2)