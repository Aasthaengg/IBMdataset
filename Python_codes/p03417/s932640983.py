N, M = map(int, input().split())

#四つ角：4回
#辺上：6回
#内側：9回
if N==1 and M==1:
    print(1)
elif N == 1 or M ==1:
    #端：2回
    #その他：3回
    print(max(N-2,M-2))
else:
    print((N-2)*(M-2))
