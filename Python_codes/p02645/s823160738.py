import random
n=input()
m = list(n)
a = random.randint(0,len(n)-3)
print(m[a]+m[a+1]+m[a+2])
