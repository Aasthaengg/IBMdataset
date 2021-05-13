
N = int(input())
S = list(input()) #１文字ずつ

ans=0
for i in range(1,N):
    X = S[0:i]
    Y = S[i:N]
    cnt=0
    # print('X.,Y:', X,Y)

    als=[chr(ord('a') + i) for i in range(26)]
    for al in als:
        if (al in X) and (al in Y):
            cnt+=1
    ans=max(ans,cnt)
print(ans)
