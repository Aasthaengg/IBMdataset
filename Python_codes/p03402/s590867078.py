A,B = map(int,input().split())

d = {}
for i in range(50):
    d[i] = ["."]*100
for i in range(50,100):
    d[i] = ["#"]*100
a = 1
b = 1

for i in range(10):
    if a == B:
        break
    for j in range(50):
        if a == B:
            break
        else:
            d[i*2][j*2] = "#"
            a += 1
    
        
        
for i in range(10):
    if b == A:
        break
    for j in range(50):
        if b == A:
            break
        else:
            d[i*2+51][j*2] = "."
            b += 1
    

print("100 100")
def l_to_str(l):
    s = ""
    for x in l:
        s+=x
    return s
for i in range(100):
    print(l_to_str(d[i]))