N = int(input())
A = input().split()
result = 0
count = False
while count == False:
    if (A == ([0] * N or ["0"] * N)): break
    for i in range(N):
        if (int(A[i]) % 2 != 0): count = True
        A[i] = int(A[i]) / 2
    if (count == True): break
    result += 1

print(result)