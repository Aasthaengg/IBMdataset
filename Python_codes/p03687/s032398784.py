from collections import Counter
s = input()

#文字ごとに全探索
#aaa,x,aa,x,aaaaのように、xで文字列を分解したときの最長要素数が答え
char_li = set(s)
ans=float('inf')
for char in char_li:
    ans=min(ans,max([len(l) for l in s.split(char)]))

print(ans)