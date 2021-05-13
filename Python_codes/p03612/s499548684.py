import math
n = int(input())
p = list(map(int, input().split()))

# 連続する部分列を数える
cnt=0
ary=[]
for i in range(n):
    if p[i]==i+1:
        cnt+=1
    else:
        ary.append(cnt)
        cnt=0
ary.append(cnt)
print(sum([math.ceil(i/2) for i in ary if i > 0]))