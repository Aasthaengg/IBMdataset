from sys import stdin
N = int(stdin.readline().rstrip())
A = stdin.readline().rstrip()
B = stdin.readline().rstrip()
C = stdin.readline().rstrip()
ans = 0 
for i in range(N):
    ans += len(set([A[i], B[i], C[i]]))-1
print(ans)