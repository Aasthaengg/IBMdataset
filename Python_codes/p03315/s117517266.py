S = input()
p = [c for c in S if c == '+']
print(len(p) - (len(S)  - len(p) ))