import copy
from collections import defaultdict

N, M = map(int, input().split())
org_arr = [list(map(int, input().split())) for _ in range(M)]
arr = copy.copy(org_arr)
arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])

count = 1
dic = {}
for i in range(len(arr)):
    dic[arr[i][1]] = count
    if i == len(arr)-1:
        break
    if arr[i][0] == arr[i+1][0]:
        count += 1
    else:
        count =1


for i in org_arr:
    ans = str(i[0]).zfill(6)+str(dic[i[1]]).zfill(6)
    print(ans)