# SoundHound Inc. Programming Contest 2018 -Masters Tournament-: B – Acrostic
S = input()
w = int(input())

word = ''

for i in range(0, len(S), w):
    word += S[i]

print(word)