from collections import defaultdict

ans,n = 0,int(input())
a_list = list(map(int,input().split()))
a_dict = defaultdict(int)
for i in range(n):
    a_dict[a_list[i]]+=1
for key,value in a_dict.items():
    if value>key:
        ans += value-key
    elif value<key:
        ans += value
print(ans)