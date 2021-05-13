#62
h,w = map(int,input().split())
c = []
for i in range(h):
    a = list(map(str,input().split()))
    c.append(a)
    c.append(a)
    
for i in range(2*h):
    print("".join(c[i]))
    
