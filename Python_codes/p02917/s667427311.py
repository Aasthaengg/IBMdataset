N = int(input())
B = list(map(int, input().split()))
B.insert(0, B[0])
A = []
for n in range(1, N):
    A.append(min(B[n-1], B[n]))
    
print(sum(A)+B[N-1])