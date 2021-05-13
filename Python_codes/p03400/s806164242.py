n = int(input())
d, x = map(int,input().split())
al = []
for _ in range(n):
    al.append(int(input()))

total = 0
for a in al:
    i = 0
    while i * a + 1 <= d:
        i += 1
    total += i
print(total+x)

