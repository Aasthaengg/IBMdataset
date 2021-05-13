s = input()

dic = {}
for i in range(len(s)):
  if s[i] in dic:
    dic[s[i]] += 1
  else:
    dic[s[i]] = 1

if len(dic) == 1:
  if len(s) == 1:
    print('YES')
  else:
    print('NO')

elif len(dic) == 2:
  if len(s) == 2:
    print('YES')
  else:
    print('NO')

else:
  first = 'a'
  second = 'b'
  for k, v in dic.items():
    if  v > dic[first]:
      if k != first:
        second = first
        first = k

    elif v > dic[second]:
      if k != second and k != first:
        second = k


  tmp = first + second
  dic[first] -= 1
  dic[second] -= 1
  ans = 'YES'

  for i in range(1, len(s) - 1):
    if tmp[i-1] == 'a':
      if tmp[i] == 'b':
        if dic['c'] == 0:
          ans = 'NO'
          break
        else:
          dic['c'] -= 1
          tmp += 'c'

      if tmp[i] == 'c':
        if dic['b'] == 0:
          ans = 'NO'
          break
        else:
          dic['b'] -= 1
          tmp += 'b'

    elif tmp[i-1] == 'b':
      if tmp[i] == 'a':
        if dic['c'] == 0:
          ans = 'NO'
          break
        else:
          dic['c'] -= 1
          tmp += 'c'

      if tmp[i] == 'c':
        if dic['a'] == 0:
          ans = 'NO'
          break
        else:
          dic['a'] -= 1
          tmp += 'a'

    elif tmp[i-1] == 'c':
      if tmp[i] == 'a':
        if dic['b'] == 0:
          ans = 'NO'
          break
        else:
          dic['b'] -= 1
          tmp += 'b'

      if tmp[i] == 'b':
        if dic['a'] == 0:
          ans = 'NO'
          break
        else:
          dic['a'] -= 1
          tmp += 'a'

  print(ans)

