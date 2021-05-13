N = int(input())
A = []
B = []
for _ in range(N):
    a, b = list(map(int, input().split()))
    A.append(a)
    B.append(b)

if N % 2== 0:
    A.sort()
    med_A = (A[N//2] + A[N//2 - 1])/2
    B.sort()
    med_B = (B[N//2] + B[N//2 - 1])/2
    print(int((med_B-med_A) * 2 + 1))
else:
    A.sort()
    med_A = A[(N-1)//2]
    B.sort()
    med_B = B[(N-1)//2]
    print(int(round(med_B) - round(med_A) + 1))