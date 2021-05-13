import math
N = int(input())

div_num = []
for i in range(1,int(math.sqrt(N))+1):
    if N%i== 0:
        div_num.append((i,N//i))
if div_num == []:
    div_num = [(1,N)]
min_div_num = 10**12
for i in div_num:
    min_div_num = min(sum(i),min_div_num)
print(min_div_num-2)