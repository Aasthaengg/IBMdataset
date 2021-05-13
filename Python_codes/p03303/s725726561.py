S = input()
w = int(input())

moji = ''

for i in range(len(S)):
    if i%w==0:
        moji += S[i]
print(moji)