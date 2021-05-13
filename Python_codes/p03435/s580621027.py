C = list(list(map(int,input().split())) for _ in range(3))
a = C[0][0] + C[1][1] + C[2][2]
b = C[0][2] + C[1][0] + C[2][1]
c = C[0][1] + C[1][2] + C[2][0]
if a == b == c:
    print("Yes")
else:
    print("No")