def l(): return list(map(int, input().split()))
def m(): return map(int, input().split())

def main():
  c = [0]*3
  for i in range(3):
    c[i] = l()
  for i in range(2):
    x = c[2][i+1] - c[2][i]
    for j in range(2):
      if c[j][i+1] - c[j][i] != x:
        print('No')
        exit()
  print('Yes')

  
if __name__ == '__main__':
  main()