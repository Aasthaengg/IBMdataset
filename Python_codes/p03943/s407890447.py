num=list(map(int,input().split()))
num.sort()
print('Yes' if num[2]==(num[0]+num[1]) else 'No')