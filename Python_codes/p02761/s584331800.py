#C
import sys
n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
sc.sort(key=lambda x: x[0])
ans = [-1] * n
for i in range(m):
    #すでに値が入っているAND値が同じではない
    if ans[sc[i][0]-1] != -1 and ans[sc[i][0]-1]!=sc[i][1]:
        print(-1)
        sys.exit() 
    ans[sc[i][0] - 1] = sc[i][1]
#1桁目が-1未定義 -> n=2以上は最小値が1ダメ
if ans[0] == -1 and n >= 2:
    ans[0] = 1
#1桁目が0　　　　-> n=2以上は定義できない。
if ans[0] == 0 and n>=2:
    print(-1)
    sys.exit()
for i in ans:
    if i == -1:
        print(0, end="")
    else:
        print(i,end="")