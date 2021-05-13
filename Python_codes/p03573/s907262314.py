lis = list(map(int, input().split()))
lis.sort()
if lis[0]==lis[1]: print(lis[2])
else: print(lis[0])