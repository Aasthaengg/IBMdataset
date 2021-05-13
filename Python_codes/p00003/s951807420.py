# -*- coding:utf-8 -*-

if __name__ == '__main__':

	N = int(raw_input())

	for i in range(0,N):

		a, b, c = raw_input().split()
		triangle = [int(a),int(b),int(c)]
		triangle.sort()
		
		if(triangle[2]**2 == triangle[0]**2 + triangle[1]**2):
			print 'YES'
		else :
			print 'NO'