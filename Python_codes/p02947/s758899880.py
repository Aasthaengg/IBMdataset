n=int(input())
s=[]
for i in range(n):
  tmp_input = input()
  tmp_input = ''.join(sorted(tmp_input))
  s.append(tmp_input)

results = {}
for i in range(n):
  if s[i] in results:
    results[s[i]] += 1
  else:
    results[s[i]] = 1

def choose2(n):
  return n*(n-1)//2

count = 0
for value in results.values():
  count += choose2(value)
print(count)