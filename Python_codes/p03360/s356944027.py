li = list(map(int,input().split()))
k = int(input())
li.sort()
ans = li[2]*(2**k)+li[0]+li[1]
print(ans)