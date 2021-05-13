input_line = raw_input().split()
a = int(input_line[0])
b = int(input_line[1])
print a/b,
print a%b,
print ('%.5f' % (float(a)/float(b)))