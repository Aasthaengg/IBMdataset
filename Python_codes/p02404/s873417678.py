import sys

while True :
	h,w = map(int,raw_input().split())
	if h==0 and w==0:
		break
	else :
		i,j=[0,0]
		for num in range(h):
			j = 0
			if i==0 or i==h-1 :
				print '#'*w
			else :
				for nnum in range(w):
					if j==0 : 
						sys.stdout.write('#')
						j += 1
					elif j==w-1 :
						sys.stdout.write('#\n')
						j += 1
					else :
						sys.stdout.write('.')
						j += 1
			i += 1
	print''