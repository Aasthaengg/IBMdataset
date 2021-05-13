A,B = map(int,input().split())

ans = list()
ans.append(A+B)
ans.append(A-B)
ans.append(A*B)
print(max(ans))