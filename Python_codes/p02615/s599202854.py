N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
pro = A[0]
for i in range(0, N-2):
    pro += A[1+(i//2)]
print(pro)