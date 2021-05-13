A = int(input())
B = int(input())

# 10^100って扱えるっけ
result = ''
if (A > B):
  result = 'GREATER'
elif (A < B):
  result = 'LESS'
else:
  result = 'EQUAL'

print(result)
