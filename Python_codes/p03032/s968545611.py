N,K = map(int,input().split())
V = list(map(int,input().split()))
V.insert(0,0)
V.append(0)

ans = -10**7
for i in range(min(N,K)+1):
    for j in range(min(N-i,K-i)+1):
        for k in range(min(i+j,K-i-j)+1):
            T = V[:i+1]
            T.extend(V[N-j+1:])
            T.sort()
            for t in range(k):
                if T[t] < 0:
                    T[t] = 0
                else:
                    break
            ans = max(ans,sum(T))

print(ans)