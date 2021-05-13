import sys

n = int( sys.stdin.readline() )

i = 0
while i < n:
    i = i+1
    x = i
    if x%3 == 0 or str(x).find( "3" ) > -1:
        sys.stdout.write( " " + str(i) )
        continue
print

sys.exit(0)