from sys import stdin
N,M,K = [int(x) for x in stdin.readline().rstrip().split()]
flag = False
for a in range(N+1):
    for b in range(M+1):
        if (N-a)*b + (M-b)*a == K:
            flag = True
if flag:
    print("Yes")
else:
    print("No")