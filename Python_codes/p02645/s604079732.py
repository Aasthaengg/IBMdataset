import random
S=input()
L=len(S)
rand=random.randint(0,len(S)-3)
print(S[rand:rand+3])