s = str(input())
x = 'CODEFESTIVAL2016'
ans = 0
for i,j in zip(s,x):
    if i != j:
        i = j
        ans += 1
print(ans)