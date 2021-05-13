# coding: utf-8

house_count = int(input().rstrip())
house_list = sorted(map(int, input().rstrip().split(" ")))
ans = house_list[house_count-1] - house_list[0]
print(ans)