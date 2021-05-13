n = int(input())
a = list(input().split())
a1 = ['']*(n//2 + n%2)
a2 = ['']*(n//2)

for i in range(n):
	if i%2 == 0:
		a1[i//2] = a[i]
	else:
		a2[-i//2] = a[i]

if n%2 != 0 and n != 1:
	ans = ' '.join(a1[::-1]) + ' ' + ' '.join(a2[::-1])
elif n%2 == 0:
	ans = ' '.join(a2) + ' ' + ' '.join(a1)
else:
	ans = a[0]
print(ans)