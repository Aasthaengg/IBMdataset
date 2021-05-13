from itertools import product
A,B,C,D = list(input())
for x in product(("+","-"),repeat=3):
    if eval(A+x[0]+B+x[1]+C+x[2]+D)==7:
        print(A+x[0]+B+x[1]+C+x[2]+D+"=7")
        break