from sys import stdin

S = list(stdin.readline().rstrip())
print('Yes' if S[2]==S[3] and S[4]==S[5] else 'No')