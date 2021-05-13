import sys
b = input()
if not ( b == 'A' or b == 'T' or b == 'G' or b == 'C' ): sys.exit()

if b == 'T': print('A')
if b == 'A': print('T')
if b == 'C': print('G')
if b == 'G': print('C')