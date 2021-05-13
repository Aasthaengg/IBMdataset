import sys
input = sys.stdin.readline

x,y = list(map(int,input().split()))
nl = [[1,3,5,7,8,10,12],[4,6,9,11],[2]]
nd = {1:0,1:0,3:0,5:0,7:0,8:0,10:0,12:0,4:1,6:1,9:1,11:1,2:2}
print('Yes' if y in nl[nd[x]] else 'No')
