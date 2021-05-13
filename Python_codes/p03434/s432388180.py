N = int(input())
a = input().split()
a = [int(i) for i in a]

Bob=0
Alice=0

a.sort(reverse=True)
for i in range(N):
    if i%2 == 1:
        Bob = Bob + a[i]
    else:
        Alice = Alice + a[i]
print(Alice-Bob)
