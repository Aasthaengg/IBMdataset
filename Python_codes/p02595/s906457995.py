n, d = map(int, input().split())
x = list()
y = list()
cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    c = a**2 +b**2
    if c <= d**2:
        cnt += 1 
print(cnt)