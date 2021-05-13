x, y = list(map(int,input().split()))
G = [[1,3,5,7,8,10,12], [4,6,9,11]]
ans = 'No'
for g in G:
    if x in g and y in g:
        ans = 'Yes'
print(ans)
