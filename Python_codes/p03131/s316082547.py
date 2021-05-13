k,a,b = map(int,input().split())
if a>=b or k<a:
    print(1+k)
else:
    s = k - a + 1
    t = s//2
    if s%2==0:
        print(max(1+k, a + (b-a)*t))
    else:
        print(max(1+k, a + (b-a)*t+1))