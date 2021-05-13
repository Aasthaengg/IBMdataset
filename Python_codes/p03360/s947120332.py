li = list(map(int,input().split()))
K = int(input())
li.sort(reverse = True )
li[0]=li[0]*2**K
ans = sum(li)
print(ans)