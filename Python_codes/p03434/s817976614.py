N = int(input())
a = list(map(int,input().split()))
Alice = 0
Bob = 0
for i in range(N):
    if(i % 2 == 0):
        Alice += max(a)
        a.remove(max(a))
    else:
        Bob += max(a)
        a.remove(max(a))
print(Alice-Bob)