K,A,B=list(map(int,input().split()))
hand=0
if B-A<=2:
    print(K+1)
    exit()
K=K-A+1
if K%2==1:
    hand=1+int((K-1)/2)*(B-A)
else:
    hand=int(K/2)*(B-A)
print(hand+A)