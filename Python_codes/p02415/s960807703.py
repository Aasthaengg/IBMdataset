in_line = raw_input()
buf = ""
for i in xrange(len(in_line)):
    if in_line[i].isupper():
        buf += in_line[i].lower()
    elif in_line[i].islower():
        buf += in_line[i].upper()
    else:
        buf += in_line[i]
print buf