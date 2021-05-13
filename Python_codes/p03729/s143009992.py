word=input().split()
if word[0][-1]==word[1][0] and word[1][-1]==word[2][0]:
    ans="YES"
else:
    ans="NO"
print(ans)