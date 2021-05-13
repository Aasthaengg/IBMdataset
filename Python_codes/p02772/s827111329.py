N = int(input())
A = list(map(int, input().split()))


i = 0

for i in range(len(A)):
    if (A[i] % 2 != 0 or (A[i] % 3 == 0 or A[i] % 5 == 0)):
        continue
    else:
        print('DENIED')
        exit()


print('APPROVED')
