S = list(input())
defaultDic = {"+":0,"-":0}
for i in S:
    defaultDic[i] += 1
res = defaultDic["+"] * 1 + defaultDic["-"] * ( -1 )
print(res)