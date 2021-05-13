S = input()
original_str = "keyence"
length = 7

for i in range(len(original_str)+1):
  str1 = original_str[:i]
  str2 = original_str[i:]
  if S[:len(str1)] == str1 and (S[::-1])[:len(str2)] == str2[::-1]:
    print("YES")
    exit()
    
print("NO")