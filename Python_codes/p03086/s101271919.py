S = input()
acgt = ["A","C","G","T"]
mylist = [0]

for i in range(len(S)):
    if S[i] in acgt:
        mylist.append(mylist[-1]+1)
    else:
        mylist.append(0)
print(max(mylist))