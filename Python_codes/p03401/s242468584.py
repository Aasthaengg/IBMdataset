n = int(input())
a = list(map(int, input().split()))
s = 0
ol = 0
for i in a:
	s += abs(i-ol)
	ol = i
s += abs(ol)
a.insert(0,0)
a.append(0)
for i in range(1,n+1):
	if (a[i-1] < a[i] < a[i+1]) or (a[i-1] > a[i] > a[i+1]):
		print (s)
	else:
		print (s-min(abs(a[i-1]-a[i]),abs(a[i]-a[i+1]))*2)
