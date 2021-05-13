#template
def inputlist(): return [int(j) for j in input().split()]
#template
N = int(input())
a = input().split()
li = []
s = 1
for i in range(1,N):
    if a[i] != a[i-1]:
        li.append(s)
        s = 1
        continue
    if a[i] == a[i-1]:
        s +=1
if s != '':
    li.append(s)
n = len(li)
ans = 0
for i in range(n):
    l = li[i]
    ans += l//2
print(ans)