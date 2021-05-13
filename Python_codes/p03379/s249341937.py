N = int(input())
X = list(map(int, input().split()))
A = sorted(X)
med1 = A[N // 2 - 1] 
med2 = A[N // 2]
for x in X:
    if x <= med1:
        print(med2)
    else:
        print(med1)