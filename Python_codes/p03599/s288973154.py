a,b,c,d,e,f = map(int,input().split())
"""
100a 水 <= 30
100b 水 <= 30
c 砂糖 <= 30
d 砂糖 <= 30
e 100gにとける砂糖の量
f 最大質量

全探索の時間ですか！？ 高々 30*30*1000*1000 工夫っすれば  oK.
"""
ans = 0
ansl = [a*100, 0]
for a_times in range(f//(a*100) + 1):
	a_g = a_times * a * 100
	for b_times in range(f//(b*100) + 1):
		b_g = b_times * b * 100
		for c_times in range(f//c + 1):
			c_g = c_times * c
			for d_times in range(f//d + 1):
				d_g = d_times * d
				targ = a_g+b_g+c_g+d_g
				if targ > f:
					break
				elif targ != 0:
					if (a_g+b_g)//100*e >= c_g+d_g:
						if (c_g+d_g)/targ > ans:
							ans = (c_g+d_g)/targ
							ansl = [targ, c_g+d_g]
print(*ansl)