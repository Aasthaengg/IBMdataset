N=int(input())
c=str(input())
rnum=c.count('R')
wnum=c.count('W')

rnum_front=c.count('R', 0, rnum)
wnum_back=c.count('W', N-wnum, N)

if rnum > wnum:
    print(wnum-wnum_back)
else:
    print(rnum-rnum_front)
