n = int(input())

a = [int(input()) for _ in range(n)]
a_sorted = sorted(a, reverse=True)

if a_sorted[0] == a_sorted[1]:
    for i in range(n):
        print(a_sorted[0])
else:
    for i in range(n):
        if a[i] != a_sorted[0]:
            print(a_sorted[0])
        else:
            print(a_sorted[1])
