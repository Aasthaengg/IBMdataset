n = int(input())
l = list(map(int,input().split()))
max_height = 0
res = 0
for i in l:
    if i >= max_height:
        max_height = i
    else:
        res += (max_height-i)
print(res)