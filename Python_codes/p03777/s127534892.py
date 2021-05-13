a, b = input().split()
ans = "HD"
index = ans.index(b)
if ans.index(a):
    print(ans[index-1])
else:
    print(ans[index])
