a = int(input())
b = int(input())
ans = [0]*3
ans[a-1] = 1
ans[b-1] = 1
print(ans.index(0) + 1)
