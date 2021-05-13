n = int(input())
s_list = list(input().split())
# print(s_list)

l = []
for s in s_list:
    # print(s)
    if not s in l:
        l.append(s)
# print(l)
if len(l) == 4:
    print("Four")
else:
    print("Three")