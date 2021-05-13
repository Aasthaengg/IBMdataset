
x,y = map(int,input().split())
grp = [0]*13
grp[2] = 1 # 2 をグループ番号１に
for i in [4,6,9,11]: # 4,6,9,11 をグループ番号２に
  grp[i] = 2
print('Yes' if grp[x] == grp[y] else 'No')
