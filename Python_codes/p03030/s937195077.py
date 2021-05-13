i = int(input())
score = [input().split() for s in range(i)]
s_list = sorted(score)

for i in range(len(s_list)):
  for j in reversed(range(i+1, len(s_list))):
    if s_list[j-1][0] == s_list[j][0] and int(s_list[j-1][1]) < int(s_list[j][1]):
      s_list[j-1], s_list[j] = s_list[j], s_list[j-1]

for s in s_list:
  for index,sc in enumerate(score):
    if s == sc:
      print(index+1)