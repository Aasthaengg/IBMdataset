A_lists = [map(int, input().split()) for _ in range(3)]
num_dict = {}
for n1, A_list in enumerate(A_lists):
    for n2, a in enumerate(A_list):
        num_dict[a] = (n1, n2)

N = int(input())
B_list = [int(input()) for _ in range(N)]
bing_ar = [[False, False, False] for _ in range(3)]

keys = num_dict.keys()
for b in B_list:
    if b in num_dict:
        n1, n2 = num_dict[b]
        bing_ar[n1][n2] = True

if ((sum(bing_ar[0]) == 3) or (sum(bing_ar[1]) == 3) or (sum(bing_ar[2]) == 3)) or \
    ((bing_ar[0][0] == True) and (bing_ar[1][0] == True) and (bing_ar[2][0] == True)) or \
    ((bing_ar[0][1] == True) and (bing_ar[1][1] == True) and (bing_ar[2][1] == True)) or \
    ((bing_ar[0][2] == True) and (bing_ar[1][2] == True) and (bing_ar[2][2] == True)) or \
    ((bing_ar[0][0] == True) and (bing_ar[1][1] == True) and (bing_ar[2][2] == True)) or \
    ((bing_ar[0][2] == True) and (bing_ar[1][1] == True) and (bing_ar[2][0] == True)):
    print('Yes')
else:
    print('No')
    

