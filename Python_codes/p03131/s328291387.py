k, a, b = map(int, input().split()) 
biscet = 1

rate = (b-a)/2

if ( rate > 1):
    k-=(a-1)
    biscet+=(a-1)
    biscet += int(k/2) * (b-a)
    biscet += k%2
    
else:
    biscet += k    

print(biscet)