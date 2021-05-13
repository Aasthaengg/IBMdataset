def getDivCount( a, b, x ):
    count=0
    if a!=0 :
        count+=b//x-(a-1)//x
    else:
        count+=b//x+1
    return count

a,b,x = map(int, input().split())
print( getDivCount(a,b,x) )