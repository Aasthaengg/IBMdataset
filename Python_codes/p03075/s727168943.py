import itertools
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
for x,y in itertools.permutations([a,b,c,d,e],2):
    if x-y > k:
        print(":(")
        exit()
print("Yay!")