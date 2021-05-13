a,v=map(int,raw_input().split())
b,w=map(int,raw_input().split())
t=input()

if v<=w:
	print "NO"
elif t*(v-w)>=abs(a-b):
	print "YES"
else:
	print "NO"
