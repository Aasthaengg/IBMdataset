a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
import itertools

cannot=False
for x,y in itertools.combinations([a,b,c,d,e],2):
    if y-x>k:
        cannot=True
if cannot:
    print(":(")
else:
    print("Yay!")