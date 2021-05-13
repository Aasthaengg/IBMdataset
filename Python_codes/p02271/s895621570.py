n = int(input())
A = list(map(int, input().split()))

values = set({})
for num in range(1 << n):
    count = 0
    for k in range(n):
        if num & (1 << k) == 1 << k:
            count += A[k]
    # print(num, count)
    values.add(count)

m = int(input())
Q = list(map(int, input().split()))
for q in Q:
    if q in values:
        print("yes")
    else:
        print("no")
