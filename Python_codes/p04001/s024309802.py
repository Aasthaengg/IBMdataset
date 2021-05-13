
def main():

    s = str( input() )
    s_l = len(s)
    ans = 0
    for i in range( 2 ** (s_l - 1) ):
        x_i = [ 0 for i in range( s_l - 1 ) ]
        x_i_ = list( format( i , 'b' ) )
        x_i[ len( x_i ) - len( x_i_ ) : ] = x_i_

        start = 0
        goal = 0
        for j in range( len(x_i) ):
            if x_i[j] == '1':
                goal = j + 1
                ans += int( s[start:goal] )

                #print(start,goal,int( s[start:goal] )  )

                start = goal
        goal = s_l
        ans += int( s[ start:goal ] )

        #print(start , goal,int( s[start:goal] )  )
    
    print( ans )

main()