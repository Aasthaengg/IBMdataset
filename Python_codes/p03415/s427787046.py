import itertools
def main():
  a = []
  for i in range(3):
    s = input()
    a.append(s[i])
  print('{}{}{}'.format(a[0],a[1],a[2]))
if __name__ == '__main__':
  main()