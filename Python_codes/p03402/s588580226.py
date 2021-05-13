A, B = map(int, input().split())
X = [["#"]*100 for _ in range(50)]+[["."]*100 for _ in range(50)]
A -= 1
B -= 1
for i in range(10):
    for j in range(50):
        if A > 0:
            X[10+i*2][j*2] = "."
            A -= 1
            
for i in range(10):
    for j in range(50):
        if B > 0:
            X[60+i*2][j*2] = "#"
            B -= 1
            
print(100, 100)
for x in X:
    print(*x, sep = "")