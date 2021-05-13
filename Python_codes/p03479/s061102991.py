import math

x,y = map(int,input().split())
"""
値をどんどん2倍していって、それがyを超えないかを検証し、越えなければカウントを増やす
"""

count = 0
origin = x
while True:
  if origin <= y:
    count+=1
    origin = origin * 2
  else:
    break
    
print(count)