N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
mn=abs(A-(T-H[0]*0.006))
c=0
for i in range(N):
    if mn>abs(A-(T-H[i]*0.006)):
        mn=abs(A-(T-H[i]*0.006))
        c=i
print(c+1)