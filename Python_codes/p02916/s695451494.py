N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A = [0] + A
B = [0] + B
C = [0] + C

ans = 0
for i, a in enumerate(A[1:-1]):
    i = i+1 
#    print(i, A[i], A[i+1])
#    print(B[a])
    ans += B[a]
    if A[i+1] - A[i] == 1:
#        print('C', C[a])
        ans += C[a]
ans += B[A[-1]]
print(ans)