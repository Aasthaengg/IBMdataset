H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

if H > W:
    H, W = W, H

count = [0] * 26
for i in a:
    for j in i:
        count[ord(j) - ord('a')] += 1

# print (count)
lst = [0] * 5
for c in count:
    lst[4] += c // 4
    c %= 4
    lst[2] += c // 2
    c %= 2
    lst[1] += c

# print (lst)
flag = False
if H >= 2 and W >= 2:
    if (H // 2) * (W // 2) <= lst[4]:
        lst[2] += (lst[4] - (H // 2) * (W // 2)) * 2 
        # print ('A')
        # print (lst)
        if ((H % 2) * (W // 2)) + ((W % 2) * (H // 2)) == lst[2] and (H % 2) * (W % 2) == lst[1]:
            flag = True
            # print ('B')

if H == 1 and W % 2 == 0:
    if lst[1] == 0:
        flag = True
if H == 1 and W % 2 == 1:
    if lst[1] == 1:
        flag = True

if flag:
    print ('Yes')
else:
    print ('No')