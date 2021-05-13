N,X = map(int,input().split())
L = list(map(int,input().split()))
cnt = 0
i = 0
cnt += L[i]
while cnt<=X:
    i += 1
    if i<N:
        cnt += L[i]
    else:break
print(i+1)