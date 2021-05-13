s = input()
ans = 0
l = len(s)
for i in range(2**(l-1)):
  nums = [s]
  idx = 0
  #print(f'i={i}')
  for j in range(l-1):
    if i>>j&1:
      a = s[idx:j+1]
      b = s[j+1:]
      #print(f'j={j}')
      #print(f'idx={idx}, a={a}, b={b}')
      idx = j+1
      nums[-1] = a
      if b != '':
        nums.append(b)
  ans += sum(list(map(int, nums)))
  #print(nums)
  #print('----------------')
print(ans)