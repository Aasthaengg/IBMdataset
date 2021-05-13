N=int(input())
x=list(map(int,input().split()))
sort_dict={}
count=0
from collections import deque

_x = deque()
for i in sorted(enumerate(x), key=lambda x:x[1]):
    sort_dict[i[0]]=count#昔のインデックスi[0]=count(新しいインデックス)
    _x.append(i[1])#並び替えの要素を追加
    count+=1
_x=list(_x)

cut=N//2-1

for i in range(N):
    #抜く数字はx[i].x[i]の_xにおけるインデックスが分かれば、答えは出る
    #i:ソート前のインデックス
    #sorted_dict[i]:ソートあとインデックス=
    sort_idx=sort_dict[i]
    if sort_idx<=cut:
        print(_x[cut+1])
    else:
        print(_x[cut])
