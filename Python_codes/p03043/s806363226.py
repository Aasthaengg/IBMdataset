
[N,K] = list(map(int,input().split()))

nino_ijo=[0]*21
for i in range(21):
    nino_ijo[i] = 2**i
# print('nino:', nino_ijo)

out=0
for i in range(1,N+1):
    # print('i:',i)
    for j in range(21):
        if i*(2**j) >= K:
            out += (1/N) * ((1/2)**j)
            break
    # print('out:',out)
print(out)
