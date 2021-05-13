k = list(map(int, input().split()))
n = k[ 0 ]
m = k[ 1 ]

bigArray = []
smallArray = []
for i in range ( n ) :
    bigArray.append( list(map(int, input().split())) )
for i in range ( m ) :
    smallArray.append( int(input()) )

for i in range ( n ) :
    answerPerRow = 0
    for j in range ( m ) :
        answerPerRow += bigArray[ i ][ j ] * smallArray[ j ]
    print( answerPerRow )