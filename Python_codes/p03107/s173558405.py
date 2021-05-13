S = list(input())
N = len(S)
print(N-abs(S.count('0')-S.count('1')))