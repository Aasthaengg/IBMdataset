n =int(input())
a = list(map(int, input().split()))

ans = []

for i in range(n):
    j = n-i
    count = 0
    itr = 2
    while(1) :
        s =j * itr
        if s > n :
            break
        count += ans[n-1-(s-1)]
        itr +=1
    j = n -i
    if (count%2 == a[j-1]):
        ans.append(0)
    else:
        ans.append(1)

ans.reverse()
print(sum(ans))
for i,j in enumerate(ans):
    if j == 1:
        print(i+1, end=" ")
        
