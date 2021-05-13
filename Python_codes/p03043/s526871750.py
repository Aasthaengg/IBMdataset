from fractions import Fraction
N , K = list(map(int,input().split()))
denom_list = []
Z=0


def detame_keisan( N , K , i ):
    kijun = K
    score = i
    count = 0
    
    while score < kijun:
        count += 1
        score = ( score *  2 )
    return N * (2 ** count)

for i in range( 1,N+1 ):
    X = detame_keisan( N , K , i)
    denom_list.append( X )

for item in denom_list:
    #Z += 1/item
    Z += Fraction(1, item)
#print( Z)
print( float( Z ))