
N = int(input())

cnt=0
for A in range(1,N):
    for B in range(1,N):
        if A*B >= N:
            break
        else:
            cnt+=1
print(cnt)