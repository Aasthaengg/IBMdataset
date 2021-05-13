K, A, B = map(int, input().split())
if K <= A-1+1:
    print(K+1)
    exit()

print(max(K+1, A + (B-A)*((K - (A-1))//2) + (K-A+1) % 2))
