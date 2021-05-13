N,M,K = map(int,input().split())
ans = 'No'
for x in range(M+1):
    if M-2*x == 0:
        if K%N == 0:
            ans = 'Yes'
            break
        else:
            continue
    else:
        if (K-N*x)%(M-2*x) == 0 and 0 <= (K-N*x)/(M-2*x) <= N:
            ans = 'Yes'
            break
        else:
            continue
print(ans)