n = int(input())
a = list(map(int,input().split()))
count = 1
for i in range(n):
    if a[i]%2 == 0:
        count *= 2
print(3**n-count)