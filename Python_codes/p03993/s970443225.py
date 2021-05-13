N = int(input())
a = [int(x)-1 for x in input().split()]

ans = 0
for i in range(N) :
    if a[a[i]] == i :
        ans += 1

print(ans//2)
