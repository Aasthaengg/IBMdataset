# C - たくさんの数式
from itertools import product
S = input()
n = len(S)-1
total =0
for i in list(product(["","+"],repeat=n)):
    bag=""
    for ind,val in enumerate(S):
        if ind ==0:
            bag+=val
        else:
            bag+=i[ind-1]+val
    total +=eval(bag)        
print(total)