A,B = map(int,input().split())
B_ans = 1
count = 0
while B>B_ans:
  B_ans = B_ans+A-1
  count = count+1
print(count)