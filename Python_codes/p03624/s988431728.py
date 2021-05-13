S=input()
x="None"
num=[False for i in range(26)]
for i in range(len(S)):
    num[ord(S[i])-ord("a")]=True

for j in range(26):
    if not num[j]:
        x=chr(j+ord("a"))
        break

print(x)
