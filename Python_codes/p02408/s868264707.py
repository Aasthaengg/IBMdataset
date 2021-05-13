S = []
H = []
C = []
D = []

n = int(input())
for i in range(n):
    mark, num = [x for x in input().split()]
    if mark == 'S':
        S.append(int(num))

    elif mark == 'H':
        H.append(int(num))

    elif mark == "C":
        C.append(int(num))

    else: #D
        D.append(int(num))


for i in range(1,14):
    if not i in S:
        print("S", i)
for i in range(1,14):
    if not i in H:
        print("H", i)
for i in range(1,14):
    if not i in C:
        print("C", i)
for i in range(1,14):
    if not i in D:
        print("D", i)