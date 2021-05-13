S = input()

l=[]
ans = "yes"

for i in S:
    if i in l:
        ans = "no"
        break
    else:
        l.append(i)

print(ans)