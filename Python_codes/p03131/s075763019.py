K, A, B = map(int, input().split())
if B-A <= 2:
    print(K+1)
    exit()

if A+1 > K:
    print(K+1)
elif (K-A-1)//2*(B-A)+(K-A-1)%2+(A-1)+(B-A)+1 > K+1:
    print((K-A-1)//2*(B-A)+(K-A-1)%2+(A-1)+(B-A)+1)
else:
    print(K+1)