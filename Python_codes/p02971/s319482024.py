n=int(input())
s=[int(input()) for _ in range(n)]
lst=sorted(s,reverse=True)
max1=lst[0]
max2=lst[1]
for i in range(n):
    if s[i]==max1:
        print(max2)
    else:
        print(max1)