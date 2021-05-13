n = int(raw_input())

Mem = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for i in range(n):
    C = map(int, raw_input().split())
    Mem[C[0]-1][C[1]-1][C[2]-1] += C[3]

for i in range(4):
    for j in range(3):
        output = ""
        for k in range(10):
            output += ' ' + str(Mem[i][j][k])
        print output
    if i != 3: 
        print '#'*20