##### 解けた #####

A,B,C=list(map(int,input().split(" ")))

if (A+B)>=C: # 買える場合
    print("Yes")
else: # 買えない場合
    print("No")