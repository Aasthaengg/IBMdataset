k,x = map(int,input().split())

left = x - k + 1
right = x + k - 1

left = max( -1000000 , left)
right = min( 1000000 , right)

print(' '.join(list( map(str,range(left,right+1)) )))
