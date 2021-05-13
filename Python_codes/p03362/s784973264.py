n=int(input())

import math
def isPrime(num):
    if num < 2: return False
    elif num == 2: return True
    elif num % 2 == 0: return False
    for i in range(3, math.floor(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True
def callIsPrime(input_num):
    numbers = []
    for i in range(1, input_num):
        if isPrime(i):
            numbers.append(i)
    return numbers

tmp=callIsPrime(10000)
result=[]
cnt=0
for item in tmp:
    if item%5==1:
        result.append(item)
        cnt+=1
    if cnt==n:
        break
#print(len(result))
print(" ".join(map(str,result)))