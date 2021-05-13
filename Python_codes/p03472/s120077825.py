import sys
n, h = map(int, input().split())
ans = 0
ans, a, b = 0, 0, []

for _ in range(n):
    c1, c2 = map(int, input().split())
    a = max(a, c1)
    b.append(c2)
b = sorted(b, reverse=True)

def count(ans, num):
    if num.is_integer():
        ans += int(num)
    else:
        ans += int(num)+1
    print(ans)
    sys.exit()
    

i = 0
while h > 0:
    if i == len(b):
        count(ans, h/a)
    elif a >= b[i]:
        count(ans, h/a)
    else:
        h -= b[i]
        ans += 1
        i += 1
print(ans)
