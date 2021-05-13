n,m = map(int,input().split())
if(( n ==1) &( m == 1)):
    print(1)
if( (n == 1) & (m != 1)):
    print(m - 2)
if( (n != 1) & (m == 1)):
    print(n - 2)
    
if ((n != 1) &( m != 1)):
    print(n*m -(2*n + 2*m -4))