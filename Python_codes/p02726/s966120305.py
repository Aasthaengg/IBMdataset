import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,X,Y = map(int,readline().split())
ans = [0]*N
for i in range(1,N):
    for j in range(i+1,N+1):
        dist = min(j-i,abs(i-X)+1+abs(j-Y),abs(i-Y)+1+abs(j-X))
        ans[dist]+=1
print('\n'.join(str(n) for n in ans[1:]))