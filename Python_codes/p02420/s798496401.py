import sys

def shuffle( cards ):
	h = int( sys.stdin.readline() )
	cards = cards[ h : ] + cards[ 0 : h ]
	return cards

while True:
	cards = sys.stdin.readline().rstrip()
	if '-' == cards:
		break
	m = int( sys.stdin.readline() )
	for i in range( m ):
		cards = shuffle( cards )
	print( cards )