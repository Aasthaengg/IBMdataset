n=int(input())
s=input()
count=0
for i in range(n):
  str_1=s[0:i-1]
  str_2=s[i-1:n]
  if count<len(set(str_1)&set(str_2)):
    count=len(set(str_1)&set(str_2))
print(count)      