s = list(input())
ans = []
count_r = 0
count_l = 0
for i in range(len(s)):
  if s[i] == 'R':
    if i == 0:
      count_r += 1
      ans.append(0)
    elif s[i-1] == 'L':
      if (count_r + count_l) % 2 == 0:
        ans.pop()
        ans.append((count_r+count_l)//2)
        ans.append((count_r+count_l)//2)
        for _ in range(count_l-1):
          ans.append(0)
      else:
        ans.pop()
        k = (count_r+count_l)//2
        if count_r > k:
          a = (count_r-1)%2
          if a == 0:
            ans.append(k+1)
            ans.append(k)
            for _ in range(count_l-1):
              ans.append(0)
          else:
            ans.append(k)
            ans.append(k+1)
            for _ in range(count_l-1):
              ans.append(0)
        else:
          a = (count_l-1)%2
          if a == 0:
            ans.append(k)
            ans.append(k+1)
            for _ in range(count_l-1):
              ans.append(0)
          else:
            ans.append(k+1)
            ans.append(k)
            for _ in range(count_l-1):
              ans.append(0)
      count_r = 1
      count_l = 0
      ans.append(0)
    else:
      count_r += 1
      ans.append(0)
  elif s[i] == 'L':
    count_l += 1
if (count_r + count_l) % 2 == 0:
        ans.pop()
        ans.append((count_r+count_l)//2)
        ans.append((count_r+count_l)//2)
        for _ in range(count_l-1):
          ans.append(0)
else:
  ans.pop()
  k = (count_r+count_l)//2
  if count_r > k:
    a = (count_r-1)%2
    if a == 0:
      ans.append(k+1)
      ans.append(k)
      for _ in range(count_l-1):
        ans.append(0)
    else:
      ans.append(k)
      ans.append(k+1)
      for _ in range(count_l-1):
        ans.append(0)
  else:
      a = (count_l-1)%2
      if a == 0:
        ans.append(k)
        ans.append(k+1)
        for _ in range(count_l-1):
          ans.append(0)
      else:
        ans.append(k+1)
        ans.append(k)
        for _ in range(count_l-1):
          ans.append(0)
print(*ans)