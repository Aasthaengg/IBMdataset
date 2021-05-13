K, A, B = map(int, input().split())

if B-A<=2:
    print(K+1)
else:
    print(A+(K-A+1)%2+(K-A+1)//2*(B-A))