# a-b-c-dのようなつながり方でないとアウト
connected_town_dict = {i:set() for i in range(1,5)}

for i in range(3):
    a,b = map(int, input().split())
    connected_town_dict[a].add(b)
    connected_town_dict[b].add(a)

for i in range(1,5):
    if len(connected_town_dict[i])!=1 and len(connected_town_dict[i])!=2:
         print("NO")
         break
else:
    print("YES")