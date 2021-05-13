A,B,C,K=list(map(str,input().split()))
if K[-1]=='0' or K[-1]=='2' or K[-1]=='4' or K[-1]=='6' or K[-1]=='8':
    ans=int(A)-int(B)
    if len(str(ans))>18:
        print('unfair')
    else:
        print(ans)
else:
    ans=int(B)-int(A)
    if len(str(ans))>18:
        print('unfair')
    else:
        print(ans)