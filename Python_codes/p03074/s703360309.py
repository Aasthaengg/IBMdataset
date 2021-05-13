n, k = map(int, input().split())
s = str(input())
head = s[0]

counts = []
_hd = head
_cnt = 0
for _s in s:
  if _s == _hd:
    _cnt += 1
  else:
    counts.append(_cnt)
    _hd = _s
    _cnt = 1
else:
  counts.append(_cnt)

acc = [0]
for c in counts:
  acc.append(acc[-1] + c)
if s[-1] == '0':
  acc.append(acc[-1])

ans = 1
if len(counts) <= 2*k:
  ans = len(s)
else:
  if head == '1':
    for i in range(2*k+1, len(acc)+1, 2):
      p = acc[i] - acc[i - (2*k+1)]
      ans = max(ans, p)
  else:
    for i in range(2*k, len(acc)+1, 2):
      p = acc[i] - acc[max(0, i-(2*k+1))]
      ans = max(ans, p)

print(ans)