A,B,C = list(map(int,input().split()))
K = int(input())

ans = 0

for i in range(K):
    if A < B * (2**i) < C * (2**(K-i)):
        ans += 1
    else:
        pass

if ans > 0:
    print("Yes")
else:
    print("No")
