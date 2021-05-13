N = int(input())
S = input()
cnt = 0
ans = [0]
for i in S:
    if i =='I':
        cnt+=1
        ans.append(cnt)
    if i == 'D':
        cnt-=1
        ans.append(cnt)
print(max(ans))