A,B = map(int,input().split())

print(100,100)
L=[]
for i in range(50):
    L.append(["#" for j in range(100)])
for i in range(50):
    L.append(["." for j in range(100)])

A-=1

for i in range(50):
    for j in range(25):
        if A>0:
            L[i*2][j*2] = "."
            A -=1
B-=1

for i in range(50):
    for j in range(25):
        if B>0:
            L[51 + i*2][j*2] = "#"
            B-=1
for i in range(100):
    print("".join(L[i]))