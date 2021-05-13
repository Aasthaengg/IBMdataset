N = int(input())
A = list(map(int,input().split()))
c = 0

for n in range(N):
    if (n+1)%2 == 1 :
        if A[n]%2 == 1 :
            c = c + 1

print(c)