s = input()
n = int(input())
a=''
for i in range(len(s)):
  if i%n==0:
    a+=s[i]
print(a)