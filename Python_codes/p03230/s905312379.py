n = int(input())

yn=1
a=2
while True:
    if n==yn:
        print('Yes')
        break
    elif yn>n:
        print('No')
        exit()
    else:
        yn+=a
        a+=1

a-=1
k=n*2//a
s=[[a] for i in range(k)]

l = [0]*n

for i in range(a):
    s[0].append(i+1)
    l[i]+=1

for i in range(1,k):
    for j in range(i):
        s[i].append(s[j][i])
    while len(s[i]) - 1 != s[i][0]:
        for m in range(s[i-1][-1]-1,n):
            if l[m] == 0:
                s[i].append(m + 1)
                l[m] += 1
                if len(s[i]) - 1 == s[i][0]:
                        break
        if len(s[i]) - 1 != s[i][0]:
            for m in range(s[i-1][-1]-1,n):
                if l[m] == 1:
                    s[i].append(m + 1)
                    l[m] += 1
                    if len(s[i]) - 1 == s[i][0]:
                        break
        break

print(k)

for i in range(len(s)):
    for j in range(len(s[i])):
        if j==len(s[i])-1:
            print(s[i][j])
        else:
            print(s[i][j], end=' ')