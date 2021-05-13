n = int(input())
s = input()
x = int(s, 2)
pcx = s.count("1")
pc1 = x % (pcx - 1) if pcx > 1 else 0
pc2 = x % (pcx + 1)

def f(j):
    cnt = 0
    while j:
        j %= bin(j).count("1")
        cnt += 1
    return cnt

for i, y in enumerate(s):
    k = n - 1 - i
    if y == "0":
        print(f((pc2 + pow(2, k, pcx + 1)) % (pcx + 1)) + 1)
    elif pcx > 1:
        print(f((pc1 - pow(2, k, pcx - 1)) % (pcx - 1)) + 1)
    else:
        print(0)

