import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
S,T=read().rstrip().decode().split()
print(sum(s!=t for s,t in zip(S,T)))