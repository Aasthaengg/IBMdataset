def main():
    n , y = map( int , input().split() )
    y = y // 1000
    flag = 0
    ans = [ -1 , -1 , -1 ]
    for a in range( n + 1 ):
        # 10yen
        sum = a * 10
        if sum > y:
            break

        for b in range( n + 1 - a ):
            #5yen
            sum_ = sum
            sum_ += b * 5
            if sum_ > y:
                break
            if y - sum_ == n - a - b:
                flag = 1
                ans[0] = a
                ans[1] = b
                ans[2] = n - a - b
                break
        if flag:
            break
    print( *ans )

main()