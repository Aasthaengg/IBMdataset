a,b = map(str,input().split())
ans = 0
for i in range(int(a),int(b)+1):
    j = str(i)[::-1]
    if str(i) == str(j):
        ans+=1
print(ans)