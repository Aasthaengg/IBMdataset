N=int(input())
X=list(map(int, input().split()))
XX = sorted(X)
med1 = XX[N//2 - 1]
med2 = XX[N//2]
for i in range(N):
    if X[i] <=med1:
        print(med2)
    else:
        print(med1)
