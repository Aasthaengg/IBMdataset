from sys import stdin
A,B,K=[int(x) for x in stdin.readline().rstrip().split()]
for i in range(K):
    if i%2==0:
        if A%2 != 0:
            A-=1
        B+=(A/2)
        A-=(A/2)
    else:
        if B%2 != 0:
            B-=1
        A+=(B/2)
        B-=(B/2)
print(int(A),int(B))