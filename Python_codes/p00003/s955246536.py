num = int( input() )
for j in range( num ) :
    inputed = list(map(int, input().split()))
    maxIndex = inputed.index( max(inputed) )
    judger = 0;
    for k in range( 3 ) :
        if( maxIndex != k ) :
            judger += inputed[ k ] ** 2
    if judger == ( inputed[ maxIndex ] ** 2 ) :
        print("YES")
    else :
        print("NO")