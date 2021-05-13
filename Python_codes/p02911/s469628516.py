n,k,q = map(int,input().split())
start = [k for i in range(n)]
a = [0 for i in range(n)]
for i in range(q):
    a[int(input())-1] += 1


for i in range(n):
    t = start[i] - (q - a[i])
    if t <= 0:
        print("No")
    else:
        print("Yes")
