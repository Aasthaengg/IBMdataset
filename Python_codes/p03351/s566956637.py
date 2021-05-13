li=list(map(int,input().split()))
if abs(li[0]-li[2])<=li[3] or (abs(li[0]-li[1])<=li[3] and abs(li[1]-li[2])<=li[3]):
    print('Yes')
else:
    print('No')
