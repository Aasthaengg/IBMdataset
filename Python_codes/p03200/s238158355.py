S = input()
n = S.count('W')
print(sum([i for i in range(len(S)) if S[i]=='W']) - n*(n-1)//2)
