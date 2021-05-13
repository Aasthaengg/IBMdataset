N=list(map(int,input().split()))
print("YES" if len(set(N))==4 and (1 in N and 9 in N and 7 in N and 4 in N) else "NO")