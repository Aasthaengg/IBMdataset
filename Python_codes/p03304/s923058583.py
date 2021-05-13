# -*- coding: utf-8 -*-

def kitaichi(an,ad):
	c=0
	if ad==0:
		c=an*1.0
	elif an - ad>0:
		c=(an-ad)*2.0
	elif an == 0:
		return 0
	else:
		c=0
			
	return c/(an**2)


# スペース区切りの整数の入力
n, m, d = map(int, raw_input().split())
print kitaichi(n,d)*(m-1)


