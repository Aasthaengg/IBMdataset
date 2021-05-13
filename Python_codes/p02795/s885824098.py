import sys
def I(): return int(sys.stdin.readline().rstrip())
H,W,N = [I() for _ in range(3)]
ans,mod = divmod(N,max(H,W))
print(ans if mod==0 else ans+1)
