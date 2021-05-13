a = input()
b = input()
c = input()
x = 0
y = 0
z = 0
q = "a"
ans = 0
while 1:
    
    if q == "a":
        if len(a) == x:
            ans = "A"
            break
        q = a[x]
        x += 1
        
    elif q == "b":
        if len(b) == y:
            ans = "B"
            break
        q = b[y]
        y += 1
        
    else:
        if len(c) == z:
            ans = "C"
            break
        q = c[z]
        z += 1
        
print(ans)