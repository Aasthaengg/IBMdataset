N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
if A[0] != 0:
    print(-1)
else:
    count = 0
    prev = 0
    for i in range(1, N):
        temp = A[i] - prev
        if 0 < temp:
            if 2 <= temp:
                print(-1)
                break
            if A[i] == prev + 1:
                count += 1
            else:
                count += A[i]
            prev = A[i]
        else:
            count += A[i]
            prev = A[i]
    else:
        print(count)
