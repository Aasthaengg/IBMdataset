a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

from itertools import permutations, combinations,combinations_with_replacement,product
ls = [a,b,c,d,e]
comb = list(combinations(ls,2))

flag=0
for i in range(10):
    sa = abs(comb[i][1] - comb[i][0])
    if sa > k:
        flag=1

if flag==0:
    print("Yay!")
else:
    print(":(")