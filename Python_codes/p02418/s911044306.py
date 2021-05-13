s = raw_input()
p = raw_input()
s += s

if str.find(s, p) != -1:
  print "Yes"
else:
  print "No"