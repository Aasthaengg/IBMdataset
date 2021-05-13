s=input()
ans='None'
dic='abcdefghijklnmopqrstuvwxyz'
for i in range(26):
    if dic[i] not in s:
        ans=dic[i]
        break
print(ans)
