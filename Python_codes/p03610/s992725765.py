s = list(input())

moji = []
if len(s)%2 == 0:
    for i in range(len(s)//2):
        moji.append(s[2*i])
else:
    for i in range((len(s)+1)//2):
        moji.append(s[2*i])
print("".join(moji))
