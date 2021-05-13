X = int(input())

l = 0
r = 10**9

while r-l>1:
    tmp = (l+r)//2
    if (tmp+1)*tmp//2 >= X:
        r = tmp
    else:
        l= tmp

print(r)