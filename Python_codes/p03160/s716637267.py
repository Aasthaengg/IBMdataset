N = int(input())
H = list(map(int, input().split()))
P = [0, abs(H[0]-H[1])]
for i in range(1, N-1):
	P.append(min(P[i-1]+abs(H[i-1]-H[i+1]), P[i]+abs(H[i]-H[i+1])))
print(P[-1])