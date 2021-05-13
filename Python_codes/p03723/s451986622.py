A,B,C = map(int, input().split())

def even(a):
	if a % 2 == 0:
		return True
	else:
		return False

cnt = 0

while even(A) and even(B) and even(C):
	if A == B and B == C:
		cnt = -1
		break
	else:
		tmp1, tmp2, tmp3 = A,B,C
		A = (tmp2+tmp3) // 2
		B = (tmp3+tmp1) // 2
		C = (tmp1+tmp2) // 2
		cnt += 1

print(cnt)

