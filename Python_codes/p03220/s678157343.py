N = int(input())
T,A=map(int,input().split())
H = list(map(int,input().split()))
minn = 10**5
min_num=0

for i in range(len(H)):
    if abs(A-(T-H[i]*0.006))<=minn:
        minn = abs(A-(T-H[i]*0.006))
        min_num = i+1
print(min_num)