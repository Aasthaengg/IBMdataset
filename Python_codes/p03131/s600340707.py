K,A,B = map(int,input().split())

if B-A < 2:
    print(1+K)
    exit()

cnt = A-1
K -= cnt
print(A+((B-A)*(K//2)+K%2))