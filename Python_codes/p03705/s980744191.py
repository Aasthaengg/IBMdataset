N,A,B = list(map(int,input().split()))
if B-A >= 0 and N != 1:
    print((B-A)*(N-2)+1)
elif B-A == 0 and N == 1:
    print(1)
else:
    print(0)