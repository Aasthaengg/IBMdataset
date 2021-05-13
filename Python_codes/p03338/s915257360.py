N = int(input())
S = input()
counter = 0
for i in range(1,N):
    sbe = set(S[:i])
    saf = set(S[i:])
    counter = max(counter,len(sbe&saf))
print(counter)
