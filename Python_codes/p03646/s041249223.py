import sys
def I(): return int(sys.stdin.readline().rstrip())

K = I()
q,r = K//50,K % 50
A = [49+q-i for i in range(50)]
B = [50+q-i for i in range(50)]
C = A[r:] + B[:r]

print(50)
print(*C)
