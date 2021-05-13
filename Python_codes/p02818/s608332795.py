T,A,K = map(int,input().split())
sta = T + A - K
if sta <= 0:
    print("0 0")
elif sta >= A:
    print(str(T-K) +" "+str(A))
else:
    print("0 " + str(sta))