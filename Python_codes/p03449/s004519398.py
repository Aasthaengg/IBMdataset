N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(max(sum(A[:n+1]+B[n:]) for n in range(N)))