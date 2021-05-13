s = input()
s = list(s)
t = input()
t = list(t)
import string
alpha = string.ascii_lowercase
alpha = list(alpha)
dic_1 = {}
dic_2 = {}
for a in alpha:
  dic_1[a] = 0
  dic_2[a] = 0
s_result = []  
t_result = []
for _ in s:
  if dic_1[_] == 0:
    i = max(dic_1.values()) + 1
    dic_1[_] = i
    s_result.append(i)
  else:
    s_result.append(dic_1[_])
for _ in t:
  if dic_2[_] == 0:
    i = max(dic_2.values()) + 1
    dic_2[_] = i
    t_result.append(i)
  else:
    t_result.append(dic_2[_])    
check = True

for i in range(len(s_result)):
  if s_result[i] != t_result[i]:
    check = False  
if check == True:
  print("Yes")
else:
  print("No")
    

