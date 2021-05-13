S = input().strip()
if len(S)<26:
    for i in range(97,123):
        if chr(i) not in S:
            print(S+chr(i))
            break
else:
    flag = 0
    for i in range(24,-1,-1):
        if S[i]<S[i+1]:
            a = S[i]
            for j in range(25,i,-1):
                if S[j]>a:
                    print(S[:i]+S[j])
                    flag = 1
                    break
            if flag==1:break
    if flag==0:
        print(-1)