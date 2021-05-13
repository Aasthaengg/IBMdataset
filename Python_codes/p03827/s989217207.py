n = int(input())
s = input()

slist = [0]
sval = 0
for i in s :
    if i == "I":
        sval += 1
        slist.append(sval)
    else:
        sval -= 1
        slist.append(sval)
print(max(slist))