import sys
input = sys.stdin.readline
#-------------
S = input()
#-------------
S = list(S)
count = S.count("o")
print(int(700+100*count))