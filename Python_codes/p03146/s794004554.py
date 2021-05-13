s=int(input())
def calc(n):
  if n % 2 == 0:
    return n / 2
  else:
    return 3*n +1
ans = []
ans.append(s)
for i in range(1000001):
  if calc(ans[i]) in ans:
    print(len(ans) +1)
    exit()
  else:
    ans.append(int(calc(ans[i])))