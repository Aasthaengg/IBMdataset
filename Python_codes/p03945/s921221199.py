S = input()
change = 0
flag = S[0]
for i in S[1:]:
    if i != flag:
        change +=1
        flag = i
print(change)