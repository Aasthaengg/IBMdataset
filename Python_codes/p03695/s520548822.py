import sys
 
n = int(sys.stdin.readline().rstrip())
a = [int(x) for x in sys.stdin.readline().rstrip().split()]
 
counter = [0,0,0,0,0,0,0,0]
counter_wild = 0
 
for x in a:
    if x < 400:
        counter[0] += 1
    elif x < 800:
        counter[1] += 1
    elif x < 1200:
        counter[2] += 1
    elif x < 1600:
        counter[3] += 1
    elif x < 2000:
        counter[4] += 1
    elif x < 2400:
        counter[5] += 1
    elif x < 2800:
        counter[6] += 1
    elif x < 3200:
        counter[7] += 1
    else:
        counter_wild += 1
 
c = len(list(filter(lambda x: x != 0,counter)))
 
if counter_wild == 0:
    minimum_num = c
    maximum_num = c
else:
    minimum_num = max(1,c)
    maximum_num = c+counter_wild
 
print(minimum_num,maximum_num)