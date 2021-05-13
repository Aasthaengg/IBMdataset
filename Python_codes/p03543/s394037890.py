s = raw_input()
print 'Yes' if (s[:-1] == s[0]*3) or (s[1:] == s[1] * 3)  else 'No'