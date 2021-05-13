n = int(input())
s = str(input())
dic = {}
for i in s:
    dic.setdefault(i,0)
    dic[i] += 1
#print(dic)
move = {}
ans = []
cnt = 0
for i in s:
    dic[i] -= 1
    move.setdefault(i,0)
    move[i] += 1
    if dic[i]>0 and move[i]>0:
        if i not in ans:
            ans.append(i)
    elif dic[i]==0:
        if i in ans:
            ans.remove(i)
    cnt = max(cnt,len(ans))
print(cnt)