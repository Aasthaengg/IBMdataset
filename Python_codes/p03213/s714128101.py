n = int(input())
D = [0]*(n+1)

def check_div_n(div_list, n):
  return len([d for d in div_list if d>=n and d!=0])

for i in range(2, n+1):
  check_n = i
  for j in range(2, n+1):
    while check_n%j==0:
      D[j] += 1
      check_n = check_n//j
      
ans = check_div_n(D, 74) + \
      (check_div_n(D, 4)-1)*check_div_n(D, 14) + \
      (check_div_n(D, 2)-1)*check_div_n(D, 24) + \
      check_div_n(D, 4)*(check_div_n(D, 4)-1)//2 * \
      (check_div_n(D, 2)-2)
  
print(ans)