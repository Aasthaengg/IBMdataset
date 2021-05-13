# C - たくさんの数式
S =(input())
n = len(S)-1
total = 0
for i in range(2**n):
    bag = ""
    for ind,val in enumerate(S):
        bag+=val
        if ((i>>ind)&1):
            bag+="+"
    total+=eval(bag)
print(total)