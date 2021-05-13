N = int(input())

ans = 0
for n in range(1,int(N/2)+1):
    if 2*n+1 > N:
        break
    for i in range(1,int(N**(1/2)/2)+1):
        for j in range(i+1,int(N**(1/2)/2)+1):
            for k in range(j+1,int(N**(1/2)/2)+1):
                if 2*n+1 == (2*i+1)*(2*j+1)*(2*k+1):
                    ans += 1

print(ans)
