H,W,A,B=map(int, input().split())
S=["0"*A+"1"*(W-A)]*B+["1"*A+"0"*(W-A)]*(H-B)
print(*S, sep="\n")