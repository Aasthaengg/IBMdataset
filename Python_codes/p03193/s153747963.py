N,H,W = (int(T) for T in input().split())
Count = 0
for TN in range(0,N):
    A,B = (int(T) for T in input().split())
    if A>=H and B>=W:
        Count += 1
print(Count)