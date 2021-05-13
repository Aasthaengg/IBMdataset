a,b = map(int,input().split())
ans = []

ans.append(a+b)
ans.append(a+(a-1))
ans.append(b+(b-1))

print(max(ans))