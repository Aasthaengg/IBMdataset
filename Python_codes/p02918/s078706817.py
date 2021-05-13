import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N, K = map(int, readline().split())
S = readline().decode().rstrip()
cnt = 1
for i in range(N-1):
    if S[i] != S[i+1]:
        cnt += 1 
print(min(N-1,N-cnt+2*K))