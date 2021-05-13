import math
import sys
input = sys.stdin.readline
number, jump =input().rstrip().split()
number = int(number)
jump = int(jump)
scaffolding = input().rstrip().split()
scaffolding = list(map(int, scaffolding))
res = [0 for i in range(number)]
res[1] = abs(scaffolding[1]-scaffolding[0])
#test = [math.inf for k in range(jump)]
#test[0] = 0

for i in range(2, number):
    h=max(0,i-jump)
    res[i]=min(res[k]+abs(scaffolding[i]-scaffolding[k]) for k in range(h,i))   
    #res[i] = min(test)
    

print(res[number-1])