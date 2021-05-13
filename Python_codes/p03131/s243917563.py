K,A,B=map(int,input().split())

if B-A<=2:
    print(K+1)
else:
    if A<K:
        print((K-(A-1))//2*(B-A)+A+(K-(A-1))%2)
    else:
        print(K+1)