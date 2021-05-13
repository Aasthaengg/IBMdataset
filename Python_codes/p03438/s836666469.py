N = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

margin = 0 # b側で加算可能な回数
for a,b in zip(a_list, b_list):
    if a == b:
        continue
    elif a < b:
        margin -= (b-a)//2
    else:
        margin += a-b

if margin <= 0:
    print('Yes')
else:
    print('No')