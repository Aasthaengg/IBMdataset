S = input()
print(sum(s!=t for s,t in zip(S,S[::-1]))//2)