A,B,C,K = map(int, input().split())

if K > A+B:
    s = A-(K-A-B)
else:
    s = min(A,K)

print(s)