s = input()
moji = str()
for i in range(1,len(s)+1,2):
    moji += s[i-1]
print(moji)    