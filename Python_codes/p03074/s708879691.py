n, k = map(int, input().split())
s = input()
lis = [0]
j = 0
if s[0] == '0':
    lis.append(0)
    j = 1
#print(len(lis))
lis[j] += 1
for i in range(1,n):
    #print(len(lis))
    if s[i] != s[i-1]:
        j += 1
        lis.append(0)
    lis[j] += 1
if s[n-1] == '0':
    lis.append(0)
#print(lis)
com = [0] * (len(lis) + 1)
for i in range(len(lis)):
    com[i+1] = com[i] + lis[i]
#print(com)
ans = 0
for i in range(len(lis)):
    if i % 2 == 0:
        ans = max(ans,lis[i])
l = 0
while l < len(com):
    r = l + (2 * k + 1)
    if r >= len(com):
        r = len(com) - 1
    ans = max(ans,com[r] - com[l])
    l += 2
print(ans)
