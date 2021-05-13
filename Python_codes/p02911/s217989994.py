n,k,q = map(int,input().split())
a = []; b = [0]*n
for i in range(q):
    c = int(input())
    a.append(c)
    b[c-1] += 1
for i in b:
    if k-(q-i) <= 0:
        print("No")
    else:
        print("Yes")