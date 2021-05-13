#import time
#start = time.time()

def isPrimeNumber(a):
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True


n = int(input())
data = [int(input()) for i in range(n)]

count = 0
for a in data:
    if isPrimeNumber(a):
        count += 1
print(count)
#end = time.time()
#print(end - start)