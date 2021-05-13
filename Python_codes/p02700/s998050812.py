A,B,C,D = map(int,input().split())

while A > 0 and C > 0:
#高橋くん攻撃！
	C = C - B
	if C <=0:
		print("Yes")
		break
#青木くんの攻撃！
	A = A - D
	if A <=0:
		print("No")
		break