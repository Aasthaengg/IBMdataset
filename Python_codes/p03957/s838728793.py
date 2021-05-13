s = list(input())
cnt =0
for i in range(len(s)):
  if s[i] =='C':
    if 'F' in s[i:]:
        cnt +=1
print('Yes' if cnt >=1 else 'No')