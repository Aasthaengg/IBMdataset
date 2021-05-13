n, k, q = list(map(int, input().split()))
a = [int(input()) for i in range(q)]
member = [0] * n
for i in a:
    member[i - 1] += 1
for i in member:
    if i > q - k or k > q:
        print("Yes")
    else:
        print("No")

