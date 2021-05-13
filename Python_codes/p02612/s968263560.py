import sys
cin = sys.stdin.readline

n = int(cin())
n1000 = n % 1000
print(n1000 if n1000 == 0 else 1000 - n1000)