n,c = map(int,input().split())
info = [[0,0]]+[list(map(int,input().split())) for i in range(n)]+[[c,0]]
left_info = info[::-1]

right_ruiseki = [0]*(n+1)
left_ruiseki = [0]*(n+1)
ou_right_ruiseki = [0]*(n+1)
ou_left_ruiseki = [0]*(n+1)

for i in range(n):
  right_ruiseki[i+1] = right_ruiseki[i] + info[i+1][1] - info[i+1][0] + info[i][0]
  left_ruiseki[i+1] = left_ruiseki[i] + left_info[i+1][1] + left_info[i+1][0] - left_info[i][0]
  ou_right_ruiseki[i+1] = ou_right_ruiseki[i] + info[i+1][1] - 2*info[i+1][0] + 2*info[i][0]
  ou_left_ruiseki[i+1] = ou_left_ruiseki[i] + left_info[i+1][1] + 2*left_info[i+1][0] - 2*left_info[i][0]

#print(right_ruiseki,left_ruiseki,ou_right_ruiseki,ou_left_ruiseki)

for i in range(n):
  right_ruiseki[i+1]=max(right_ruiseki[i],right_ruiseki[i+1])
  left_ruiseki[i+1]=max(left_ruiseki[i],left_ruiseki[i+1])

#print(right_ruiseki,left_ruiseki,ou_right_ruiseki,ou_left_ruiseki)
ans = 0

for i in range(n+1):
  tmp1 = ou_right_ruiseki[i]+left_ruiseki[n-i]
  tmp2 = ou_left_ruiseki[i]+right_ruiseki[n-i]
  ans = max(tmp1,tmp2,ans)
print(ans)