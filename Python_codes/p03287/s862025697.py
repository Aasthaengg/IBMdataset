from collections import Counter

n,m = map(int,input().split())
A = list(map(int,input().split()))

B = [0]
res = 0
for a in A:
	res += a
	B.append(res%m)

C = Counter(B)
ans = 0
for c in C.values():
	ans += c*(c-1)//2

print(ans)