N,K = map(int, input().split())
A_list = [int(e) for e in input().split()]

MOD_BY = 7 + 10**9
ans = 0

for i in range(N):
    for j in range(N):
        Bi = A_list[i]
        Bj = A_list[j]
        #print(Bi,Bj,end="")
        if Bi > Bj:
            if K > 1:
                if i < j:
                    ans += (K+1)*K//2
                else:
                    ans += K*(K-1)//2
            else:
                if i > j:
                    ans += 1
                    
        ans %= MOD_BY
        #print(ans)
print(ans)