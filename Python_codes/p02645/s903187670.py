import random
S =input()

D =[]
for i in range(len(S)-2):
    D.append(i)

#print(D)

y = random.choice(D)
#print(y)
print(S[y:y+3])
