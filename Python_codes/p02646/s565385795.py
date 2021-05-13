A, V = [int(i) for i in input().split()]
B, W = [int(i) for i in input().split()]
T = int(input())

print('YES' if V > W and abs(A - B) <= T * (V - W) else 'NO')