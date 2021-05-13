import sys
readline = sys.stdin.readline

S = readline().rstrip()
T = readline().rstrip()

print(("No","Yes")[S == T[:-1]])  