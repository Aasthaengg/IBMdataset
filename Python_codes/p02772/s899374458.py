n = int(input())
A = list(map(int, input().split()))

count = 0
for i in range(n):
    if(A[i] % 2 == 0):
        if(A[i] % 3 != 0 and A[i] % 5 != 0):
            count += 1

if(count >= 1):
    print("DENIED")
else:
    print("APPROVED")
