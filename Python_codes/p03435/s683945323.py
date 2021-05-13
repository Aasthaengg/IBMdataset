C = [list(map(int, input().split())) for _ in range(3)]

def f():
    for i in range(2):
        for j in range(2):
            if C[i][j]-C[i][j+1] != C[i+1][j]-C[i+1][j+1]:
                return False
            if C[j][i]-C[j+1][i] != C[j][i+1]-C[j+1][i+1]:
                return False
    return True

if f():
    print("Yes")
else:
    print("No")