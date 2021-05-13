s=list(input())
k=int(input())

for i in range(k):
    if s[i]!="1":
        print(s[i])
        break
    elif i==k-1:
        print(s[i])
        break