n = input()
l = input().split()
ans = ""
for i in range(len(l)-1,-1,-1):
    if i == 0:
        ans += l[i]
    else :
        ans += l[i] + " "
print(ans)