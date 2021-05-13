from sys import stdin
H,W = [int(x) for x in stdin.readline().rstrip().split()]
N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
A = [ind+1 for ind,j in enumerate(A) for i in range(j)]
for i in range(H):
    if i % 2 == 0:
        for j in A[i*W:i*W+W]:
            print(j,end=" ")
    else:
        for j in A[i*W:i*W+W][::-1]:
            print(j,end=" ")
    print("")