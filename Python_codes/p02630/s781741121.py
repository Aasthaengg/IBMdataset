n = int(input())

a = list(map(int, input().split()))

d = {}
s = 0
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    
    s += i

q = int(input())

for i in range(0, q):

    b, c = map(int, input().split())

    if b in d:
        s = s - (d[b] * b) + (d[b] * c)
        if c in d:
            d[c] += d[b]
        else:
            d[c] = d[b]
        d[b] = 0
    
        print(s)
    else:
        print(s)
        


