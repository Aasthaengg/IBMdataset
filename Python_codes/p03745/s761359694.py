N = int(input())
A = list(map(int, input().split()))

count = 1
state = ""
for i in range(N-1):
    if A[i] > A[i+1] and state == "":
        state = "minus"
    elif A[i] > A[i+1] and state == "plus":
        state = ""
        count += 1
    elif A[i] > A[i+1] and state == "minus":
        continue
    elif A[i] < A[i+1] and state == "":
        state = "plus"
    elif A[i] < A[i+1] and state == "minus":
        state = ""
        count += 1
    elif A[i] < A[i+1] and state == "plus":
        continue
    else:
        continue
print(count)