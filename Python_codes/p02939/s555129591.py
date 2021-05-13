S = input()

count = 1
sentence = S[0]
i=1

while i < len(S):
    if sentence != S[i]:
        sentence = S[i]
        count += 1
        i+=1
    elif i==len(S)-1:
        break
    else:
        count += 1
        sentence = S[i:i+2]
        i+=2

print(count)

