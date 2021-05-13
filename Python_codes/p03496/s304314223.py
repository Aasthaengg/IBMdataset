N = int(input())
A = list(map(int,input().split()))
out = []
cnt = 0
Amax = max(A)
Amaxi = A.index(Amax)
Amin = min(A)
Amini = A.index(Amin)
if abs(Amax)>=abs(Amin):
    for i in range(N):
        if i==Amaxi:
            continue
        else:
            A[i] = A[i]+Amax
            out.append([Amaxi+1,i+1])
            cnt+=1
    for i in range(1,N):
        A[i] = A[i-1]+A[i]
        out.append([i,i+1])
        cnt+=1
else:
    for i in range(N):
        if i==Amini:
            continue
        else:
            A[i] = A[i]+Amin
            out.append([Amini+1,i+1])
            cnt+=1
    for i in range(1,N):
        A[N-i-1] = A[N-i]+A[N-i-1]
        out.append([N-i+1,N-i])
        cnt+=1

print(cnt)
for i in range(len(out)):
    X = out[i]
    print(*X)