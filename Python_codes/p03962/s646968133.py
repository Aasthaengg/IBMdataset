if __name__ == '__main__':
  s = input()
  a= [int(elem) for elem in s.rstrip().split(' ')]
  print(len(set(a)))