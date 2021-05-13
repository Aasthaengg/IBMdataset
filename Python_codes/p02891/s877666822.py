# -*- coding: utf-8 -*-

#整数値龍力　複数の入力
def input_multiple_number():
    return map(int, input().split())

S = input()
K = int(input())


if len(S) >= 1:
	flagtail = 0
	old_s = ""
	cnt = 0
	for s_ in S:
		if s_ == old_s:
			cnt +=1
			old_s = ""
		else:
			old_s = s_
	ans = cnt

	cnt1 = cnt
	old_s = ""

	if(K > 1 and K %2 == 0):
		S = S*2
		cnt1 = cnt
		cnt = 0
		old_s = ""
		for s_ in S:
			if s_ == old_s:
				cnt +=1
				old_s = ""
			else:
				old_s = s_

		ans = cnt1 + (cnt-cnt1)*(K-1)

	if(K > 1 and K %2 != 0):
		S = S*3
		cnt1 = cnt
		cnt = 0
		old_s = ""
		for s_ in S:
			if s_ == old_s:
				cnt +=1
				old_s = ""
			else:
				old_s = s_

		ans = cnt1 + (cnt-cnt1)*(K-1)//2
	print(ans)
else:
	print(K//2)