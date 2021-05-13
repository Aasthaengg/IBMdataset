#coding:UTF-8

W,H,x,y,r = map(int,raw_input().split())
if x - r < 0 or x + r > H or y - r < 0 or y + r > H:
    print "No"
else:
    print "Yes"