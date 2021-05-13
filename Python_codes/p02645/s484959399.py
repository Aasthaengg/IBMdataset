import random
l = list(input())
a = int(len(l)-3)
n = random.randint(0,a)
print(l[n]+l[n+1]+l[n+2])