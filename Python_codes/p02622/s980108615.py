import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
S,T=read().rstrip().decode().split()
ans=0
for s,t in zip(S,T):
    if s!=t:
        ans+=1
print(ans)