S=list(input())
sum=15-len(S)
S.sort()
for i in S:
    if i=='o':
        sum+=1
    if sum>=8:
        print("YES")
        break
    if i=='x':
        print("NO")
        break