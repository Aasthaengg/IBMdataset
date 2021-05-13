#!/usr/bin/env python3
s=input()
if s[0] == 'A' and 1 < s.find('C') < len(s) - 1 and (s[1:s.index('C')]+s[s.index('C')+1:]).islower():
    print("AC")
else:
    print('WA')
