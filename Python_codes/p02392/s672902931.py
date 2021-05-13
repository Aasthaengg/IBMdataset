#coding:utf-8
import sys
 
abc=sys.stdin.readline()
a,b,c=abc.split( ' ' )
a=int( a )
b=int( b )
c=int( c )
if a < b and b < c:
	print( "Yes" )
else:
	print( "No" )