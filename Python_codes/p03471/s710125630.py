N, Y = map(int, input().split())
ans = [-1,-1,-1]
flag=False
for i in range(N+1):
    for j in range(N-i+1):
        if (i*10000 + j*5000 + (N-i-j)*1000) == Y:
            ans = [i,j,N-i-j]
            flag =True
            break
    if flag:
        break
print('{} {} {}'.format(*ans))