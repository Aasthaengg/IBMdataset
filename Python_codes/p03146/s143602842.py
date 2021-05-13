s = int(input())

l = [0]*1000001
check = [False]*5000000

l[1] = s
ans = 0

for i in range(2, 1000000):
    if l[i-1] % 2 == 0:
        l[i] = round(l[i-1]/2)
    else:
        l[i] = 3*l[i-1]+1

for i in range(1,1000000):
    if check[l[i]]==False:
        check[l[i]]=True
    else:
        ans=i
        break

print(ans)
