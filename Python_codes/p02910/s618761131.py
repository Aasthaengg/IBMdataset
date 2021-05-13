str = input()
ans = "Yes"
for i in range(len(str)):
  if (i + 1) % 2 == 0 and str[i] not in ('L', 'U', 'D'):
    ans = "No"
  if (i + 1) % 2 == 1 and str[i] not in ('R', 'U', 'D'):
    ans = "No"
 
print(ans)