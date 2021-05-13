from itertools import combinations
N = int(input())
k = 2
while (k*(k-1))//2<N:
    k += 1
if (k*(k-1))//2!=N:
    print("No")
else:
    print("Yes")
    S = {i:[] for i in range(1,k+1)}
    cnt = 1
    for x in combinations(range(1,k+1),2):
        S[x[0]].append(cnt)
        S[x[1]].append(cnt)
        cnt += 1
    print(k)
    for i in range(1,k+1):
        print(len(S[i]),*S[i])