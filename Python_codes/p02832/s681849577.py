import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
A = list(map(int,readline().split()))
ans = 0
j = 1
for i in range(N):
    if A[i] == j:
        j+=1
    else:
    	ans += 1
if j == 1:
    print(-1)
else:
    print(ans)