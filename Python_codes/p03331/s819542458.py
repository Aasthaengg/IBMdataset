n = int(input())
l1 = []
l2 = []
b = 0
ans = float('inf')

def keta(x):
    l = []
    while(x > 0):
        l.append(x%10)
        x //= 10
    return l

for a in range(1, n):
    b = n - a
    l1 = keta(a)
    l2 = keta(b)
    ans = min(ans, sum(l1, sum(l2)))

print(ans)
