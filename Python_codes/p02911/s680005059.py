N, K, Q = map(int, input().split())
B = [0]*N
for _ in range(Q):
    a = int(input())
    B[a-1]+=1
S = sum(B)
for i in range(N):
    if S-B[i]>=K:
        print("No")
    else:
        print("Yes")