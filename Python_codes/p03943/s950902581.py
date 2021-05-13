def cin():
	return map(int,input().split())

def cino(test=False):
    if not test:
        return int(input())
    else:
        return input()
def cina():
  return list(map(int,input().split()))



a = cina()
a.sort()
if a[0]+a[1]==a[2]:
  print("Yes")
else:
  print("No")