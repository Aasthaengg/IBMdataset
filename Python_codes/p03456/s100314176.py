import math 
a,b=input().split()
c = a + b 
n_c = int(c)
if((n_c ** 0.5).is_integer()==True):
        print("Yes")
else:
    print('No')