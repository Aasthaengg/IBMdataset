x, n = map(int, input().split())

p = list(map(int, input().split()))

p.sort()

for i in range(100):
    a = x-i
    b = x+i
    if a not in p:
        print(a)
        break
    
    if b not in p:
        print(b)
        break

