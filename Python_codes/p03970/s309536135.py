s = input()
t = "CODEFESTIVAL2016"
ans = 0
for i,j in zip(s,t):
    ans += (i != j)
print(ans)