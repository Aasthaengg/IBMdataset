a,b = input().split()
c,d = input().split()
e,f = input().split()
A = [a,b,c,d,e,f]
if max(A.count('1'),A.count('2'),A.count('3'),A.count('4')) >= 3:
	print("NO")
else:
	print("YES")
