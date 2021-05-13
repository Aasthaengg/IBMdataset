a,b,k = map(int,input().split())
ans = []
ans.append(a)
ans.append(b)
for i in range(min(k,b-a)):
    ans.append(a+i)
    ans.append(b-i)
ans = list(set(ans))
ans.sort()
for i in ans:
    print(i)
# print(ans)