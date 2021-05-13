n = int(input())
l = []
for i in range(n):
    s, p = input().split()
    l.append((s, -int(p), int(i+1)))
    
L = sorted(l)
for s, p, i in L:
    print(i)