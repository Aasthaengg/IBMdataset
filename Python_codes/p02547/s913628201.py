N = int(input())
 
cnt = 0
ans = 'No'
for i in range(N):
	D1, D2 = map(int, input().split())
	if D1 == D2:
		cnt += 1
	else:
		cnt = 0
   
	if cnt > 2:
		ans = 'Yes'
		break
      
print(ans)