A,B,C = map(int,input().split())
K = int(input())
if A < B:
    if B < C * (2**K):
        print("Yes")
    else:
        print("No")
else:
    for i in range(1,K+1):
        if A < B * (2**i):
            if B * (2**i) < C * (2**(K-i)):
                print("Yes")
                break
            else:
                print("No")
                break
