N = int(input())
rel_list = map(int, input().split())

member_list = [0]*N
for rel in rel_list:
    member_list[rel-1] += 1

[print(i) for i in member_list]