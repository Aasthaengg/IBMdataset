def main():
    abcd = list( map( int , list( input() ) ) )

    for i in range( 2 ** 3 ):
        ans = str( abcd[0] )
        sum = abcd[0]
        x = i

        for j in range( 1,4 ):
                
            y = x % 2
            if y:
                sum += abcd[ j ]
                ans += '+'
            else:
                sum -= abcd[ j ]
                ans += '-'
            
            ans += str( abcd[ j ] )

            x = x // 2
        if sum == 7:
            ans += '=7'
            break
    print(ans)





main()