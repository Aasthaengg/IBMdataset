#coding:utf-8
import sys
 
WHxyr=sys.stdin.readline()
nums=WHxyr.split( ' ' )
for i in range( len( nums) ):
	nums[i] = int( nums[i] )
if (0 <= nums[2]-nums[4]) and (nums[2]+nums[4] <= nums[0]) and (0 <= nums[3]-nums[4]) and (nums[3]+nums[4] <= nums[1]):
	print( "Yes" )
else:
	print( "No" )