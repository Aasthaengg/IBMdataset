A, V = [int(x) for x in input().split()]
B, W = [int(x) for x in input().split()]
T = int(input())

if V <= W:
    print('NO')
    exit()

speed = V - W
if speed * T >= abs(A-B):
    print('YES')
else:
    print('NO')
