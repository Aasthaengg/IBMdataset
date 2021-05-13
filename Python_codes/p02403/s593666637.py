import sys

while True:
	nums = [ int( val ) for val in sys.stdin.readline().split( " " ) ]
	if 0 == nums[0] and 0 == nums[1]:
		break
	for i in range( nums[0] ):
		print( "#"*nums[1] )
	print