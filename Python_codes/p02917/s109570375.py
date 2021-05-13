import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
B = list(map(int,readline().split()))
ans = 0 
ans += B[0]
for i in range(N-2):
    ans += min(B[i],B[i+1])
ans += B[N-2]
print(ans)