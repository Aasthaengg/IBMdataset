n = int(input())
st = [[str(i) for i in input().split()] for _ in range(n)]
x = input()
r = 0
p = False
for s, t in st:
    if p:
        r += int(t)
    else:
        if s == x:
            p = True
print(r)