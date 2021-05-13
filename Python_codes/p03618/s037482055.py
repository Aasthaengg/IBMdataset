s = input()
AZ = 'abcdefghijklmnopqrstuvwxyz'
lens =len(s)
cnt = 0
for ch in AZ:
  a = s.count(ch)
  cnt += a*(a-1)//2
print(lens*(lens-1)//2 - cnt + 1)