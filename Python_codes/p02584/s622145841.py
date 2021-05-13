X,K,D = map(int,input().split())
if K*D<=abs(X):
    print(abs(X)-K*D)
elif (K-(abs(X)//D))%2==0:
    print(abs(X)%D)
elif (K-(abs(X)//D))%2==1:
    print(-(abs(X)%D-D))