S=int(input())
flag = True
n = 2
List=[S]
res = 0
while flag:
  if S % 2 == 0:
    S = S // 2
  else:
    S = 3* S +1
  if List.count(S) ==0:
    List.append(S)
  else:
    res = n
    flag = False
  n += 1
print(res)