def lucas(n):
  if(n == 0):
    return 2
  if(n == 1):
    return 1
  if(n == 25):
    return 167761
  if(n == 26):
    return 271443
  if(n == 50):
    return 28143753123
  if(n == 51):
    return 45537549124
  if(n == 75):
    return 4721424167835364
  if(n == 76):
    return 7639424778862807
  return lucas(n- 1)+ lucas(n- 2)

N = int(input())

print(lucas(N))