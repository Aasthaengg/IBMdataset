N = int(input())
A = [int(a) for a in input().split(" ")]

for i in range(N):
    if A[i] % 2 == 0:
        if A[i] % 3 != 0 and A[i] % 5 != 0:
            print('DENIED')
            exit()
print('APPROVED')