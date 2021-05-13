# 初期入力　　２０２０－０７２７　21：50
import sys
input = sys.stdin.readline  #文字列では使わない
X = int(input())
ans =0
Possible =[]
if X >=2000:
    ans =1
else:
    Possible =[(i*100,i*105) for i in range(1,21)]
    for p in Possible:
        if p[0] <= X <=p[1]:
            ans =1
            break
print(ans)