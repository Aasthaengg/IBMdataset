n = int(input())
A = [int(input())-1 for _ in range(n)]
a = A[0]
i = 1
aset = set()
while a != 1:
    a = A[a]
    if not a in aset:
        aset.add(a)
        i += 1
    else:
        print(-1)
        break
else:
    print(i)
