n = int(input())
a = list(map(int,input().split()))
Alice = 0
Bob = 0
isAlice = True
for i in range(n):
    tmp = max(a)
    a.remove(tmp)
    if isAlice:
        Alice += tmp
    else:
        Bob += tmp
    isAlice = not(isAlice)
print(Alice-Bob)