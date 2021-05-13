n = int(input())
m = 0
for _ in range(n):
    a,b = map(int, input().split())
    if m < a:
        m = a
        num = b
print(m+len(range(num)))