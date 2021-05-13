N,H = list(map(int,input().split()))
Amax = 0
Bs = []
for i in range(N):
    A,B = list(map(int,input().split()))
    Amax = max(Amax,A)
    Bs.append(B)
Bs.sort(reverse=True)
cnt = 0
flag = 0
for i in range(N):
    if Bs[i]>=Amax:
        H += -1*Bs[i]
        cnt += 1
        if H<=0:
            print(cnt)
            flag=1
            break
    else:
        break
if flag==0:
    if H%Amax==0:
        print(cnt+H//Amax)
    else:
        print(cnt+H//Amax+1)