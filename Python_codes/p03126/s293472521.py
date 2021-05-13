num,food_num = map(int,input().split())

food_dict = {}

for i in range(num):
    l = list(map(int,input().split()))
    for j in range(1,l[0]+1):
            food_dict.setdefault(l[j],0)
            food_dict[l[j]] += 1

ans = 0

for name, likes in food_dict.items():
    if likes == num:
        ans += 1

print(ans)
