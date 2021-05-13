N,A,B = list(map(int,input().split()))
another=1+1*N
ans =A
N -= A-1
ans += N//2 * (B-A)
ans += N%2
print(max(ans,another))