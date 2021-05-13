import random
S=input()
3<=len(S)<=20
x=random.randint(3,len(S))
y=x-3
print(S[y:x])