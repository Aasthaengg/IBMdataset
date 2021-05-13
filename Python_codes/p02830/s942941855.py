n = int(input())
s,t = input().split()
l=[]
for i in range(n):
    l.append(s[i]+t[i])
print(''.join(l))