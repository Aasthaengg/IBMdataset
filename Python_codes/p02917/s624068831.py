N = int(input())
B = [int(x) for x in input().split()]
Sum = B[0]+B[N-2]
for T in range(0,N-2):
    Sum += min(B[T],B[T+1])
print(Sum)