from math import ceil, log
n = int(input())
if n%2==1:
    print(0)
else:
    print(sum([n//(2*pow(5,i)) for i in range(1,ceil(log(n+1,5)))]))