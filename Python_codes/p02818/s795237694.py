A, B, K= map(int,input().split())
if A >= K :
    print(A-K,B)
    exit()
B -= K-A
if B <= 0 :
    print(0,0)
else :
    print(0,B)