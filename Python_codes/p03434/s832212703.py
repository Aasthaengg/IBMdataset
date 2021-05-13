N = int(input())
a = list(map(int, input().split()))
Alice = 0
Bob = 0
for i in range(N):
    if i % 2 == 0:
        A = max(a)
        Alice = Alice + A
        a.remove(A)
    else:
        A =max(a)
        Bob = Bob + A
        a.remove(A)
print(Alice - Bob)