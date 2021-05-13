s = input()
n = len(s)
s = list(s)
all_num = n * (n-1)/2
for i in range(97,123):
  tyouhuku = s.count(chr(i))
  all_num -= tyouhuku * (tyouhuku - 1) /2
  
print(int(all_num) + 1)
  
