N = int(input())
ls = list(map(int,input().split()))

ls.sort(reverse=True)
max1 = ls.pop(0)
if max1 < sum(ls):
    print('Yes')
else:
    print('No')
    
 