S=input()
x="None"
T="abcdefghijklmnopqrstuvwxyz"
num=[0 for i in range(26)]
for i in range(26):
    num[i]+=S.count(T[i])

for j in range(26):
    if num[j]==0:
        x=T[j]
        break

print(x)
