n = int(raw_input())
print 'Christmas' + (' ' if 25 - n > 0 else '') +' '.join(['Eve'] * (25 - n)) 