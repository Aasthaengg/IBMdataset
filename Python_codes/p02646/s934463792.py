oni_A, oni_V = map(int, input().split())
nige_B, nige_W = map(int, input().split())
T = int(input())

d = abs(oni_A - nige_B)

if (nige_W >= oni_V):
    print('NO')
else:
    time = d / (abs(oni_V - nige_W))
    if (time <= T):
        print('YES')
    else:
        print('NO')
