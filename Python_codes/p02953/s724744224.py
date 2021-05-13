N = int(input())
A = list(map(int,input().split()))
first = 0
for i in range(N):
    first = max(first,A[i])
    if A[i] < first-1:
        print("No")
        exit()

print("Yes")