n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
otarget = a[0]-1
ans = 0
ans += b[otarget]
for i in range(1, n):
	ntarget = a[i]-1
	ans += b[ntarget]
	if ntarget - otarget == 1:
		ans += c[otarget]
	otarget = ntarget
print(ans)