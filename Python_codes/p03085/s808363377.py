import sys
b = input()
if not ( b == 'A' or b == 'T' or b == 'G' or b == 'C' ): sys.exit()
base = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }

print(base[b])