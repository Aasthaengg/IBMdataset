s = str(input())
n = len(s)
ans = 0
j = n-1
for i in range(n):
    if i>=j:
        break

    if s[i]=='x' and s[j]=='x':
        j-=1
        continue
    elif s[i]=='x' and s[j]!='x':
        ans +=1
        continue
    while i<j:
        if s[j]=='x':
            j-=1
            ans +=1
        elif s[i]==s[j]:
            j-=1
            break
        else:
            print(-1)
            exit()


print(ans)