n = input()
ans = sum(map(int,list(n)))
ans = max(ans,int(n[0])-1+(len(n)-1)*9)
print(ans)