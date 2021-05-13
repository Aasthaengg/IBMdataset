import sys

def shuffle( cards ):
	h = int( sys.stdin.readline() )
	n = len( cards )
	s = ""
	t = ""
	for i in range( h ):
		s += cards[i]
	for i in range( h, n ):
		t += cards[i]
	t += s
	return t

while True:
	cards = sys.stdin.readline().rstrip()
	if '-' == cards:
		break
	m = int( sys.stdin.readline() )
	for i in range( 0, m ):
		cards = shuffle( cards )
	print( cards )