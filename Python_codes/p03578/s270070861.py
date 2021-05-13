from collections import Counter

n = int(input())
d_input=list(map(int,input().split()))
m=int(input())
t_input=list(map(int,input().split()))

d_count = Counter(d_input)
t_count = Counter(t_input)

for key,value in t_count.items():
    if key not in d_count:
        print('NO');exit()
    if d_count[key]<value:
        print('NO');exit()
print('YES')
