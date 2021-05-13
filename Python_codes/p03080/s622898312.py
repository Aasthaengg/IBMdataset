N = int(input())
s = input()

RBlist = list(s)

#print(type(N))

r=RBlist.count('R')

b=N-r
if b<r:
    print("Yes")
else:
    print("No")