k = int(input())
str1 = "ACL"
str2 = "ACL"
for i in range(k-1):
  str1 = "".join([str1,str2])
print(str1)