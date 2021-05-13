n = int(input())
a = list(map(int, input().split())) 
b = list(map(int, input().split())) 
c = list(map(int, input().split())) 

manzoku = 0
for i in range(n):
    manzoku += b[a[i]-1]
    #print(b[a[i]-1])
    
    if( i > 0):
        if( a[i-1]+1 == a[i] ):
            manzoku += c[a[i-1]-1]
            #print('+'+str(c[a[i-1]-1]))
#print('')
print(manzoku)