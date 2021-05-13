o = input()
e = input()

ans = ['' for _ in range(len(o)+len(e))]
for i in range(len(o)):
  ans[i*2] = o[i]
for i in range(len(e)):
  ans[i*2+1] = e[i]
print(''.join(ans))
