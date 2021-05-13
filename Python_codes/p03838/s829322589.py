x, y = map(int, input().split())
ans = []
if y-x>=0:
    ans.append(y-x)
if -y-x>=0:
    ans.append(-y-x+1)
if y+x>=0:
    ans.append(y+x+1)
if -y+x>=0:
    ans.append(-y+x+2)
print(min(ans))
