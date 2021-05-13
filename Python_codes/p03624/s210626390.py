import string
a=string.ascii_lowercase

S=list(input())

for i in range(26):
    if a[i] not in S:
        ans=a[i]
        break
    if i==25:
        ans="None"
print(ans)
