import sys
base = ['SUN','MON','TUE','WED','THU','FRI','SAT']
S = input()

if not ( S in base ): sys.exit()

print(7 - base.index(S))