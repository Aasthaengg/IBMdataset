def i():
	return int(input())
def i2():
	return map(int,input().split())
def s():
	return str(input())
def l():
	return list(input())
def intl():
	return list(int(k) for k in input().split())

n = i()
s = {}
for i in range(n):
	S,P = map(str,input().split())
	s[i+1] = [S, -int(P)]

note = sorted(s.items(), key=lambda x: x[1][0])
note.append( (10, ["LOL", 10] ) )
memo = note[0][1][0]
a = []
for i in note:
	if memo != i[1][0]:
		memo = i[1][0]
		a = sorted(a, key=lambda x: x[1][1])
		for j in range(len(a)):
			print(a[j][0])
		a = []
		a.append(i)
	else:
		a.append(i)