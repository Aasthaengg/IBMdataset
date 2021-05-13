N = int(input())
A = list(map(int, input().split()))

increase = True
equal = True
start = True
count = 1

for i, a in enumerate(A):
    if i > 0:
        if equal:
            if a > A[i-1]:
                increase = True
                equal = False
            elif a < A[i-1]:
                increase = False
                equal = False
        else:
            if increase:
                if a < A[i-1]:
                    count += 1
                    equal = True
                    # print(i)
            else:
                if a > A[i-1]:
                    count += 1
                    equal = True
                    start = True
                    # print(i)

print(count)
