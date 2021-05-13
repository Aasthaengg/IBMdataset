s=input()
w=int(input())
ans=[s[0]]
k=w
while k<len(s):
    ans.append(s[k])
    k+=w
print("".join(ans))
