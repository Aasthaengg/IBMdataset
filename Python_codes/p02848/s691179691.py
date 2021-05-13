n = int(input())
s = input()
for i in range(len(s)):
  if ord(s[i])+n <= ord("Z"): 
    print(chr(ord(s[i])+n), end="")
  else:
    print(chr(ord(s[i])+n-26), end="")   
print()