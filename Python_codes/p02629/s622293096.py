def f(l, n):
	ans = []
	for i in range(l):
	  ans.append(chr(n % 26 + ord('a')))
	  n//=26
	print(''.join(reversed(ans)))

n = int(input())
val = 26
adds = 0
lastval = 0
cnt = 1
while val < n:
  lastval = val
  val = (val*26)+26
  cnt+=1
f(cnt, n-lastval-1)