N = int(input())
abc = [list(map(int, input().split())) for i in range(N)]
 
A = [0]
B = [0]
C = [0]
for i in range(N):
    a = abc[i][0] + max(B[-1], C[-1])
    b = abc[i][1] + max(A[-1], C[-1])
    c = abc[i][2] + max(A[-1], B[-1])
    A += [a]
    B += [b]
    C += [c]
print(max(A[-1], B[-1], C[-1]))