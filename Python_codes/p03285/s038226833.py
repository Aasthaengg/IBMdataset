N = int(input())
l = []
for i in range(25):
    for j in range(25):
        l.append(i * 4 + j * 7)
ans = 'No'
if N in l:
    ans = 'Yes'
print(ans)