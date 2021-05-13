N = int(input())
A = list(map(int, input().split()))
ab = [abs(A[0])] + [abs(A[i+1]-A[i]) for i in range(N-1)] + [abs(A[N-1])]
s = sum(ab)
print(s-sum(ab[:2])+abs(A[1]))
for i in range(1,N-1):
    print(s-sum(ab[i:i+2])+abs(A[i+1]-A[i-1]))
print(s-sum(ab[N-1:])+abs(A[N-2]))