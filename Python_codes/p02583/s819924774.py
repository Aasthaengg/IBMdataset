N = int(input())
Ls = list(map(int,input().split()))
ans = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            m = max(Ls[i],Ls[j],Ls[k])
            if Ls[i] + Ls[j] + Ls[k] - 2*m > 0 and Ls[i] != Ls[j] and Ls[i] != Ls[k] and Ls[j] != Ls[k]:
                ans += 1

print(ans)
