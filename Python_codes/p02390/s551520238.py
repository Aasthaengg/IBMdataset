S = input()
h = S / 3600
s = S % 60
m = (S - h * 3600 - s) / 60

print "%d:%d:%d" %(h,m,s)