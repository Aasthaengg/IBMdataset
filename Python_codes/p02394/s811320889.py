# coding: utf-8
# Your code here!
W, H, x, y, r = map(int, raw_input().split())
if r <= x and r <= y and x+r <= W and y+r <= H:
    print "Yes"
else:
    print "No"
