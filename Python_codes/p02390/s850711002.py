#coding:utf-8
S=int( input() )
h=int( S/3600)
S=int( S%3600)
m=int( S/60)
s=int( S%60)
print( "{}:{}:{}".format( h, m, s ) )