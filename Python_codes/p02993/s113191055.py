import sys
s = [int(n) for n in list(input())]

for i in range(3):
    if s[i] == s[i+1]:
        print('Bad')
        sys.exit(0)
print('Good')