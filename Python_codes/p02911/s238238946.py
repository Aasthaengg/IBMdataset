n,k,q = map(int,input().split())
a = [int(input()) for _ in range(q)]
b = [0] * n
for i in a:
    b[i-1] += 1
c = k - q
for j in range(n):
    if (b[j]+c) > 0:
        print("Yes")
    else:
        print("No")