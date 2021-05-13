n = int(input())
a = list(map(int,input().split()))
for i in range(n): a[i] -= 1
ans = sum([i == a[a[i]] for i in range(n)])
print(ans//2)