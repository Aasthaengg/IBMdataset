s = input()
atgc = ["A","T","G","C"]
mylist = [0]
for i in range(len(s)):
    if s[i] in atgc:
        mylist.append(mylist[-1] +1)
    else:
        mylist.append(0)
print(max(mylist))