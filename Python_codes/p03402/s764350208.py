B, A = map(int, input().split())
K = []
for i in range(50):
    K.append(["."]*100)
for j in range(50):
    K.append(["#"]*100)
a = 1
b = 1
t = 0
while(True):
    if A == a:
        break
    for i in range(0, 100, 4):
        K[t][i] = "#"
        a += 1
        if A == a:
            break
    if A == a:
        break
    t += 1
    for i in range(2, 100, 4):
        K[t][i] = "#"
        a += 1
        if A == a:
            break
    t += 1

t = 51
while(True):
    if B == b:
        break
    for i in range(0, 100, 4):
        K[t][i] = "."
        b += 1
        if B == b:
            break
    if B == b:
        break
    t += 1
    for i in range(2, 100, 4):
        K[t][i] = "."
        b += 1
        if B == b:
            break
    t += 1
print(100, 100)
for i in range(100):
    for j in K[i]:
        print(j, end="")
    print()