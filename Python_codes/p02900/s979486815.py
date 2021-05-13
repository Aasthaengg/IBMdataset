a,b = list(map(int, input().split()))

def div(n):
    divs = set([1])
    i = 2
    while i*i <= n:
        while n%i==0:
            divs.add(i)
            n//=i
        i+=1
        
    if n>1:
        divs.add(n)
        
    return divs

div_set = div(a) & div(b)

print(len(div_set))