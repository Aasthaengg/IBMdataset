N = int(input())
strings = input().split()

needs = 0
thred = int(strings[0])
for s in strings[1:N]:
  now = int(s)
  if now < thred:
    needs = needs + thred - now
  else:
    thred = now
    
print(needs)