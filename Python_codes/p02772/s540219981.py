N = int(input())
A = [int(i) for i in input().split()]
t = 0
for i in range(N):
    a = A[i]
    if a%2 == 0:
        if a%3 != 0 and a%5 != 0:
            t += 1
            break

if t == 0:
    print('APPROVED')
else:
    print('DENIED')