S = input()
c = 0
l = 0
for i in range(len(S)):
    if(S[i] == 'W'):
        c += i - l
        l += 1
print(c)
