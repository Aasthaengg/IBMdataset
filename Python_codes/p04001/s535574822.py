from itertools import permutations, combinations,combinations_with_replacement,product
s = input()
t = product(["+",""],repeat=len(s)-1)
sum=0
for i1 in t:
    calc = ""
    for j,i2 in enumerate(i1):
        calc+=s[j]+i2
    calc += s[-1]
    sum+=eval(calc)

print(sum)
