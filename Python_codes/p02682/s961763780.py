a, b, c, k = map(int, input().split(" "))

def some(a,b,c,k):
    x_a = min(k, a)
    k -= x_a
    x_b = min(k, b)
    k -= x_b
    x_c = k
    print(x_a*1+x_b*0+x_c*-1)

some(a,b,c,k)