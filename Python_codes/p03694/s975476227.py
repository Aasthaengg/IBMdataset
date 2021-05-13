N = int(input())
li = list(map(int,input().split()))	
ans = max(li)-min(li)
print(ans)