s = input()
t = input()

temp = 0
for i,j in enumerate(s):
    if(j != t[i]):
        temp += 1

print(temp)
