n, t = map(int, input().split())
A = list(map(int, input().split()))

min_a = A[0]
diff = 0
count = 0

for i in range(1, len(A)):
    if A[i] <= min_a:
        min_a = A[i]
    elif A[i] - min_a == diff:
        count += 1
    elif A[i] - min_a > diff:
        diff = A[i] - min_a
        count = 1

print(count)
    
