#coding:utf-8
import sys
 
ab=sys.stdin.readline()
a,b=ab.split( ' ' )
a=int( a )
b=int( b )
if a < b:
	print( "a < b" )
elif a > b:
	print( "a > b" )
else:
	print( "a == b" )