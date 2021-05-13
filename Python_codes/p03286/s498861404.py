n = int(input())
gu = [1]
ki = [0]
for i in range(0, 20):
  gu.append(gu[-1] + (-2)**(2 + 2*i))
  ki.append(ki[-1] + (-2)**(1 + 2*i))
ans = []
for i in range(20):
  if gu[-2-i] < n <= gu[-1-i]:
    ans.append('1')
    n-= (gu[-1-i]-gu[-2-i])
  else:
    ans.append('0')
  if ki[-1-i] <= n < ki[-2-i]:
    ans.append('1')
    n -= (ki[-1-i]-ki[-2-i])
  else:
    ans.append('0')
ans.append(str(n))
print(str(int(''.join(ans))))