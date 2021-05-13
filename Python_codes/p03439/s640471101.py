N = int(input())

rl = [0, N-1]
rl_condition = ["",""]
flag = True

for i, RL in enumerate(rl):
   print(RL)
   print("\n")
   s = input()
   rl_condition[i] = s
   if s == "Vacant":
      flag = False
      break

while flag:
   center = (rl[0] + rl[1])//2
   print(center)
   print("\n")
   s = input()
   if s == "Vacant":
      break
   elif ((center - rl[0])%2 == 1) and (s == rl_condition[0]):
      rl_condition[1] = s
      rl[1] = center
      continue
   elif ((rl[1] - center)%2 == 1) and (s == rl_condition[1]):
      rl_condition[0] = s
      rl[0] = center
      continue
   elif ((center - rl[0])%2 == 0) and (s != rl_condition[0]):
      rl_condition[1] = s
      rl[1] = center
      continue
   elif ((rl[1] - center)%2 == 0) and (s != rl_condition[1]):
      rl_condition[0] = s
      rl[0] = center
      continue
      
      
