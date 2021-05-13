n, h = map(int, input().split())
A = []
B = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)        
    B.append(b)        

maxa = max(A)
B = [b for b in B if b > maxa]
B.sort(reverse=True)

c = 0
for b in B:
    h -= b
    c += 1
    if h <= 0:
        break

if h > 0:
    c += h//maxa + (h%maxa > 0)
print(c)
