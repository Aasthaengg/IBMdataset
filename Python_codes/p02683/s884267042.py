import sys
input = sys.stdin.readline

def find_good( list , x ):
    #if ok : return 1 , not ok : return 0
    flag = 1
    for i in list:
        if i < x:
            flag = 0
            break
    return flag

def main():
    n,m,x = map( int , input().split() )
    a = []
    c = []
    for i in range(n):
        I = list( map( int , input().split() ) )
        c.append( I[0] )
        a.append( I[1:] )
    
    ans_min = sum(c)

    flag_ = 0

    #print(a)

    for i in range( 2 ** n ):
        z = i
        book_i = 0
        ans_list = [ 0 for j in range(m) ]
        ans_cost = 0

        while( z != 0 ):
            y = z % 2

            z = z // 2

            if y:
                for j in range( m ):
                    ans_list[j] += a[book_i][j]
                ans_cost += c[book_i]
            book_i += 1
        

        if find_good( ans_list , x ) and ans_min >= ans_cost:
            ans_min = ans_cost
            flag_ = 1
    
    if flag_:
        print(ans_min)
    else:
        print(-1)
    
main()