def cin():
	return map(int,input().split())

def cino(test=False):
    if not test:
        return int(input())
    else:
        return input()
def cina():
  return list(map(int,input().split()))

def ssplit():
    return list(input().split())

a = ssplit()
print("A"+a[1][0].upper()+"C")