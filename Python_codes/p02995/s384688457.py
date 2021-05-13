A,B,C,D=map(int, input().split())

# 最大公約数を求める
ans = 0
tmp1, tmp2 = C, D
while 1:
  if tmp1 % tmp2 == 0:
    ans = tmp2
    break
  else:
    tmp = tmp1 % tmp2
    tmp1 = tmp2
    tmp2 = tmp
ans = int(C*D/ans)
#print(ans)

num1 = B//C
num2 = (A-1)//C
num_C = num1-num2

num1 = B//D
num2 = (A-1)//D
num_D = num1-num2

num1 = B//ans
num2 = (A-1)//ans
num_CD = num1-num2

print(B-A+1-num_C-num_D+num_CD)