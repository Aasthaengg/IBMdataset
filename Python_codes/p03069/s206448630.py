
n = int(input())
s = input()


white = 0
for i in s:
    if(i=='.'):
        white += 1
        
# 全部黒の場合
        
ans = white

# 左からi+1 個白の場合

now = white

for i in range(n):
    if(s[i]=='#'):
        now+=1
    else:
        now-=1
    ans = min(now,ans)

print(ans)
