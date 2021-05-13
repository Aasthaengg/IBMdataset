N, Q = map(int,input().split())
S = input()+"d"
#'AC'が見つかったらCのほうに+1
count = [0]*(N+1)
for i in range(N):
    if S[i] == "A":
        if S[i+1] == "C":
            count[i+1] += count[i] + 1
        else:
            count[i+1] = count[i]
    else:
        count[i+1] = count[i]
    
#print(count)

for _ in range(Q):
    l, r = map(int,input().split())
    print(count[r-1]-count[l-1])