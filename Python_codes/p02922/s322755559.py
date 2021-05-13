import math
a,b = map(int,input().split())
count = 1
answer = 0
while count < b :
    count-=1
    count +=a
    answer +=1
print(answer)