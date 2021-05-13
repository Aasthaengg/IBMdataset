N = int(input())
H = list(map(int,input().split()))
ans=0
ans_list=[]
for i in range(N-1):
  if H[i]>= H[i+1]:
    ans +=1
  else:
    ans_list.append(ans)
    ans= 0
ans_list.append(ans)
    
    
print(max(ans_list))