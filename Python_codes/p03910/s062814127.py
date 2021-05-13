n = int(input())
i = 1
k = 0
ans = []
while k<n:
    k += i
    ans.append(k)
    i += 1
x = ans[-1]-n
for i in range(1,len(ans)+1):
    if i==x:continue
    print(i)