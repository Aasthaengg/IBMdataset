def cin():
	return map(int,input().split())

def cino(test=False):
    if not test:
        return int(input())
    else:
        return input()
def cina():
  return list(map(int,input().split()))


s = cino(True)
s+='A'
s = list(s)
cnt = -1
for i in range(len(s)-1):
    if s[i+1]!=s[i]:
        cnt += 1
print(cnt)
