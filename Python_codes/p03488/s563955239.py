# tle
# from copy import deepcopy
# s = list(input())
# a, b = map(int, input().split())
# def searchpath(pos, dir, st):
#     pos = deepcopy(pos)
#     dir = deepcopy(dir)
#     st  = deepcopy(st)
#     while len(st)>0:
#         i = st.pop(0)
#         if i == 'F':
#             if dir == 'r':
#                 pos = [pos[0]+1, pos[1]]
#             if dir == 'l':
#                 pos = [pos[0]-1, pos[1]]
#             if dir == 'u':
#                 pos = [pos[0], pos[1]+1]
#             if dir == 'd':
#                 pos = [pos[0], pos[1]-1]
#             if len(st) == 0 and pos == [a, b]:
#                 return 1
#         if i == 'T':
#             if dir == 'r' or dir == 'l':
#                 if searchpath(pos, 'u', st)==1 or searchpath(pos, 'd', st)==1:
#                     return 1
#             if dir == 'u' or dir == 'd':
#                 if searchpath(pos, 'r', st)==1 or searchpath(pos, 'l', st)==1:
#                     return 1
#             break;
#     return -1
# ans = searchpath([0,0], 'r', s)
# if ans == 1:
#     print('Yes' , flush=True)
# else:
#     print('No' , flush=True)


s = input().split('T')
a, b = map(int, input().split())

current_x = len(s[0])
current_y = 0

# for i in s[2::2]: # cant calculate order
for i in sorted([len(j) for j in s[2::2]])[::-1]:
    if current_x < a:
        current_x += i
    else:
        current_x -= i
for i in sorted([len(j) for j in s[1::2]])[::-1]:
    if current_y < b:
        current_y += i
    else:
        current_y -= i

if current_x==a and current_y==b:
    print('Yes', flush=True)
else:
    print('No', flush=True)
    
    
