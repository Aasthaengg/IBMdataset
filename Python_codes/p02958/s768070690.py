import numpy as np
N = int(input())
xlist = list(map(int, input().split()))
ans = "NO"
#降順になっていない部分の数をカウント
minus_gaps = np.count_nonzero(np.diff(xlist)<0)
#全て降順になっていれば、それでOK
if minus_gaps == 0:
    ans = "YES"
#降順でない部分が2つの場合は、その2つを入れ替えて、全て降順になるか確認
elif minus_gaps == 2:
    tmpList = np.where(np.diff(xlist)<0)
    xlist[tmpList[0][0]],xlist[tmpList[0][1]+1] = xlist[tmpList[0][1]+1], xlist[tmpList[0][0]]
    if np.count_nonzero(np.diff(xlist)<0) == 0:
        ans = "YES"
#あとは全部NO
print(ans)