A = list(input())
count = 0

for i in range(0, len(A)):
    if A[i] == "2":
        count += 1

print(count)