# ARC 061 A

def resolve():
  a, b, c = map(int, input().split())
  if c >= a and c <= b:
    print('Yes')
  else:
    print('No')

if __name__ == "__main__":
    resolve()
