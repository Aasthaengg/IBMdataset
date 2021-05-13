l='#.'*999
while 1:
 h,w=map(int,raw_input().split())
 if h==0:break
 for i in range(h):print l[i%2:w+i%2]
 print