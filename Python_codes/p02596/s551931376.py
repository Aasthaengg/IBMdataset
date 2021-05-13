K = int(input())
nana=7
kou=1
if K % 2 == 0 or K % 5 == 0:
    print(-1)
else:
    for i in range(1,K):
        if nana % K == 0:
            break
        nana = (nana * 10 + 7) % K
        kou +=1
    print(kou)