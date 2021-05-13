

n = int(input())
h = list(map(int, input().split()))

def main():
  for i in reversed(range(n-1)):
    if h[i] - h[i+1] > 1:
      return False
      exit()
    elif h[i] - h[i+1] == 1:
      h[i] -= 1
    else:
      continue
  return True

if main() == True:
  print('Yes')

else:
  print('No')