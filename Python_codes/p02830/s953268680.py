N=int(input())
a,b=input().split()
a=list(a)
b=list(b)
ab=""
for _ in range(N):
	ab+=a.pop(0)+b.pop(0)
print(ab)