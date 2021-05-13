n,m = map(int,input().split())
total = 0
if n*2 >= m:
    total += m//2
    print (total)
    exit ()
else:
    total += n
    m = m - n*2
if m >= 4:
    total += m//4
print (total)
exit ()