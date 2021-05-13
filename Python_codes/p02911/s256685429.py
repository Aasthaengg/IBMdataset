n,k,q = map(int,input().split())
lst = [int(input()) for i in range(q)]

seikai = [0]*n

for i in lst:
    seikai[i-1] += 1

for j in seikai:
    if k - (q-j) <= 0:
        print("No")
    else:
        print("Yes")