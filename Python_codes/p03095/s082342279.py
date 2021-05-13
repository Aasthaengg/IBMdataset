n=int(input())

s=input()

l=[1 for i in range(26)]

for i in range(n):
    l[ord(s[i])-ord("a")]+=1


pr=1
for i in range(26):
    pr=pr*l[i]
    pr=pr%(10**9+7)

print(pr-1)