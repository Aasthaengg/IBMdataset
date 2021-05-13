li = list(map(int, input().split()))
if li[0]+li[1] == li[2] or li[1]+li[2] == li[0] or li[2]+li[0] == li[1]:
    print('Yes')
else:
    print('No')