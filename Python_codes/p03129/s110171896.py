from math import ceil

N,K=map(int,input().split())
print("YES" if ceil(N/2)>=K else "NO")
