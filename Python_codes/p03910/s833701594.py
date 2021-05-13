#import itertools
#import bisect
import math

N = int(input())
L = [i for i in range((N+2)//2+2)]
num = math.floor(pow(2*(N-1),0.5))
    
for i in range(num,len(L)):
    if N == i*(i+1)//2:
        index = i
        Max = i*(i+1)//2
        break
    elif N < i*(i+1)//2:
        index = i
        Max = i*(i+1)//2
        break
Left = Max - N 
#print(num,Left,Max,index,L)
#acu = list(itertools.accumulate([i for i in range((N+1)//2+2)]))
#print(acu) 
#index = bisect.bisect_left(acu,N)
#print(index)
 
#if acu[index] == N:
#    Max = acu[index-1]
#else:
#    Max = acu[index]
#Left = Max - N

for i in range(1,index+1):
    if i == Left:
        continue
    print(i)