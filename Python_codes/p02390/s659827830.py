S = raw_input()
 
S = int(S)
 
h = S / 60 / 60
m = S / 60 % 60
s = S % 60 % 60
 
print "%d:%d:%d" %(h, m, s)