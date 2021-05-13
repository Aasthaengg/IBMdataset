N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
ans = 1000000
tmper = []
for i in range(N):
	tmper.append(abs(A-(T - H[i]*0.006)))
	ans = min(ans,abs(A-(T - H[i]*0.006)))
print(tmper.index(ans)+1)