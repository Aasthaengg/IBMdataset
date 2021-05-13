import sys
a = int(input())
s = input()

if not ( 2800 <= a < 5000 ): sys.exit()
if not ( 1 <= len(s) <= 10 ): sys.exit()
if not s.islower(): sys.exit()

print(s) if a >= 3200 else print('red')