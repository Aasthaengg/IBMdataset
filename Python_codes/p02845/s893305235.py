n = int(input())
a_list = list(map(int,input().split()))
a_dic = {}
for i in range(n):
  a_dic[i] = 3

ans = 1
for a in a_list:
  if a == 0:
    ans = ans * a_dic[a]
    a_dic[a] -= 1
  else:
    ans = ans * (a_dic[a] - a_dic[a-1])
    a_dic[a] -= 1
    
print(ans % (10**9 + 7))