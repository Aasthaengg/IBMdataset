s = int(input())
a = set()
while not s in a:
    a.add(s)
    if s&1 is 0: s //= 2
    else: s = 3*s+1
print(len(a)+1)
