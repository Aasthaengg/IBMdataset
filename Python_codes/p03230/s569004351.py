N = int(input())
flag = 0
for i in range(int((8*N+1)**0.5)+1):
    if i*(i-1)==2*N:
        flag = 1
        k = i
        break
if flag==0:
    print("No")
else:
    print("Yes")
    S = [[] for _ in range(k)]
    cnt = 1
    for i in range(k-1):
        for j in range(i+1,k):
            S[i].append(cnt)
            S[j].append(cnt)
            cnt += 1
    print(k)
    for i in range(k):
        print(len(S[i]),*S[i])