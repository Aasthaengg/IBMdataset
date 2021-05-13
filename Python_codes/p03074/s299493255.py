N,K = map(int,input().split())
S = input()
row = []
count = 1
flag = S[0]
for i in range(1,N):
    if S[i] != flag:
        row.append([count,flag])
        count = 1
        flag = S[i]
    else:
        count += 1
row.append([count,flag])
inst = 0
ans,temp = 0,0
left,right = 0,0
for i in range(len(row)):
    if row[i][1] == "1":
        temp += row[i][0]
    else:
        inst += 1
        if inst <= K:
            temp += row[i][0]
        else:
            temp -= row[left][0]
            if row[left][1] == "1":
                temp -=row[left+1][0]
                left += 1
            temp += row[i][0]
            left += 1
    ans = max(ans,temp)
print(ans)