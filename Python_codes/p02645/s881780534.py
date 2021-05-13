S = input()
import random
a = random.randint(1, len(S)-2)
W = S[a-1] + S[a] + S[a+1]
print(W)