N = int(input())
H = [int(x) for x in input().split()]

MAX = 0
Flag = True
for T in range(0,N):
    if H[T]>MAX:
        MAX = H[T]
    if MAX-H[T]>=2:
        Flag = False
        break
if Flag:
    print('Yes')
else:
    print('No')