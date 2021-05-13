# A - Sheep and Wolves
S,W = map(int,input().split())
ans = ['unsafe', 'safe']
print(ans[S>W])