from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0
for i in range(N):
    if A[A[i]-1] == i+1:
        ans += 1
print(ans//2)