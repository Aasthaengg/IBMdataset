S = input()

count = 1
i = 1
word = S[0]
while i < len(S):
    if word != S[i]:
        word = S[i]
        i += 1
    else:
        word = S[i: i+2]
        i += 2
    count += 1

if i != len(S):
    count -= 1
print(count)