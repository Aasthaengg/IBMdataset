S = input()
print(min(max(map(len, S.split(s))) for s in S))
