X,Y = map(int,input().split())
ans = []
ans.append(X)

while max(ans)*2 <= Y:
    ans.append(max(ans)*2)
print(len(ans))
