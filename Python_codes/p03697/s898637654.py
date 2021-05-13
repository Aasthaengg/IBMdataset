# ARC 063 A

def resolve():
  a, b = map(int, input().split())
  sum = a+b
  if sum >= 10:
    print('error')
  else:
    print(sum)


if __name__ == "__main__":
    resolve()
