a,b,c = map(int, raw_input().split())
j = 0
n = 0
for i in range(a,b+1):
    s = 1
    n = 0
    while n < c:
        n = i * s
        s = s+1
        if n == c:
            j = j + 1
print j