n,k = map(int,input().split())
a_list = list(map(int,input().split()))
a_list_2 = a_list + a_list
first_count = 0
p = 10**9 + 7
for i in range(n-1):
  for j in range(i+1,n):
     if  a_list[j] < a_list[i]:
      first_count += 1
second_count = 0    
for a in a_list:
  for i in range(n):
    if a > a_list[i]:
      second_count += 1
ans = first_count * k  +  (k-1) * k * second_count //2
print(ans % p)
    

  
