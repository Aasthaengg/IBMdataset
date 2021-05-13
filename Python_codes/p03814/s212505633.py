s = raw_input()
sinv = s[::-1]
z = len(s) -1 - sinv.find('Z')

print z - s.find('A')+1