import random
S = input()
a=len(S)
b=random.randrange(a-2)
print(S[b]+S[b+1]+S[b+2])