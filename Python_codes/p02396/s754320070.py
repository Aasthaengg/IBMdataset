import sys

i=0
while True:
	num=int( sys.stdin.readline() )
	i+=1
	if num == 0:
		break
	else:
		print( "Case {}: {}".format( i, num ) )