s = input()
sum=0
for bit in range(1 << len(s)-1):
  list_i  = [i for i in s]
  count=0
  for i in range(len(s)-1):
    if bit & (1<<i):
      count += 1
      list_i.insert(i+count,'+')
  ans=''
  for i in list_i:
    ans += i
  for i in ans.split('+'):
    sum += int(i)
print(sum)