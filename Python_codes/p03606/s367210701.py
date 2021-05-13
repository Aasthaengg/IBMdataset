n = int(input())
n_list = []
for _ in range(n):
  s,t = map(int,input().split())
  n_list.append(abs(s-t) +1)
  
print(sum(n_list))