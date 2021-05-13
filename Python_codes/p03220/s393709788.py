# B - Palace
N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

lst = []
for i in range(N):
	ref = abs(A-(T-0.006*H[i]))
	lst.append(ref)

ans = lst.index(min(lst))+1
print(ans)
