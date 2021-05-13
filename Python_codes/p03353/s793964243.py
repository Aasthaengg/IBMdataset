s = input()
k = int(input())
s_list = []
for i in range(len(s)):
  for j in range(k):
    s_list.append(s[i:i+j+1])
s_list = sorted(list(set(s_list)))
print(s_list[k-1])