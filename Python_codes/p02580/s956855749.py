H,W,M = map(int,input().split())
B = [0]*M
a,b = 0,0
HOR = [0]*H
VER = [0]*W
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    HOR[a] += 1
    VER[b] += 1
    B[i] = (a,b)

max_hor_num = -1
max_hor_set = set()
for i in range(H):
    a = HOR[i]
    if max_hor_num == a:
        max_hor_set.add(i)
    elif max_hor_num < a:
        max_hor_set = set()
        max_hor_set.add(i)
        max_hor_num = a

max_ver_num = -1
max_ver_set = set()
for i in range(W):
    a = VER[i]
    if max_ver_num == a:
        max_ver_set.add(i)
    elif max_ver_num < a:
        max_ver_set = set()
        max_ver_set.add(i)
        max_ver_num = a

#print(*max_hor_set)
#print(*max_ver_set)

empty = len(max_hor_set) * len(max_ver_set)
count = 0

if empty > M:
    print(max_hor_num+max_ver_num)
    exit()
for h,w in B:
    if (h in max_hor_set) and (w in max_ver_set):
        count += 1
    if count == empty:
        print(max_hor_num+max_ver_num-1)
        exit()
print(max_hor_num+max_ver_num)