import math
while True:
    try:
        n = int(raw_input())
    except EOFError:
        break
    if n == 0:
        break
    ls = map(int,raw_input().split())
    m = sum(ls)/float(n)
    
    tmp_tot = 0
    for k in range(n):
        tmp_tot += (ls[k]-m)**2/float(n)
    a = math.sqrt(tmp_tot)
    print a