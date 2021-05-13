A, B = map(int,input().split())

lst = [A+B, A-B, A*B]
ans = max(lst)

print(ans)