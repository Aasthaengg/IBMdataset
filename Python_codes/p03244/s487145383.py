from collections import Counter
n=int(input())
v=list(map(int,input().split()))
v1=Counter(v[::2])
v2=Counter(v[1::2])
v1[0]=0
v2[0]=0
v1_max=v1.most_common()[0]
v2_max=v2.most_common()[0]
v1_second=v1.most_common()[1]
v2_second=v2.most_common()[1]
if v1_max[0]!=v2_max[0]:
    print(n-v1_max[1]-v2_max[1])
else:
    print(min(n-v1_max[1]-v2_second[1],n-v2_max[1]-v1_second[1]))