n, k = map(int, input().split())
s = list(input())

if s[k-1]=="A":
    s[k-1]=s[k-1].lower()
elif s[k-1]=="B":
    s[k-1]=s[k-1].lower()
elif s[k-1]=="C":
    s[k-1]=s[k-1].lower()

for i in range(n):
    print(s[i],end="")