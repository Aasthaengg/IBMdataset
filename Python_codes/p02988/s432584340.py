n = int(input())
P = list(map(int, input().split()))
a = 0
for i in range(1,n-1):
    L = P[i-1:i+2]
    if not (P[i]==min(L) or P[i]==max(L)):
        a = a+1
    else:
        pass
print(a)