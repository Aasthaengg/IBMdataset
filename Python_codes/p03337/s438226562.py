A, B = map(int, input().split())

ans = []

ans.append(A+B)
ans.append(A-B)
ans.append(A*B)

print(max(ans))