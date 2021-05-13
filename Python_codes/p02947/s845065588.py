N = int(input());

dic = {};
count = 0;
for i in range(N):
  chars = list(input());
  chars.sort();
  sorted_str = "".join(chars);
  # print(sorted_str);
  
  if sorted_str in dic:
    dic[sorted_str] += 1;
    count += dic[sorted_str];
  else:
    dic[sorted_str] = 0;
  
print(count);