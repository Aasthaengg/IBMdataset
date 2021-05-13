N,K=map(int,input().split())

N+=N%2
N//=2

print("YES" if N>= K else "NO")