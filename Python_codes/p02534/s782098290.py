def read_int(x):
  return int(x)

def repeat(ch,n):
  return ''.join(list(map(lambda _: ch,range(n))))

def main():
  cnt = read_int(input())
  print(repeat("ACL",cnt))
  
main()