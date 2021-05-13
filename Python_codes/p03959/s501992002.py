N = int(input())

T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

kakutei = [-1]* N
for i,a in enumerate(A):
    if i==N-1:
        kakutei[i]= a
        continue
    if a > A[i+1]:
        kakutei[i]=a

for i,t in enumerate(T):
    if i==0:
        kakutei[i]=t
        continue
    if t > T[i-1]:
        if kakutei[i]==-1 or kakutei[i]==t:
            kakutei[i] = t
        else:
            print(0)
            exit(0)

ans = 1
for i in range(N):
    if not(kakutei[i] <= A[i] and kakutei[i] <= T[i]):
        print(0)
        exit(0)
    if kakutei[i]==-1:
        ans*= min(A[i],T[i])
        ans= ans%(10**9 +7)

print(ans)

