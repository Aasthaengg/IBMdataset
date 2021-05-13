def multipleOf9(n)-> str:
  if (n % 9) == 0:
    return 'Yes'
  return 'No'

if __name__ == "__main__":
  num = list(map(int, input().split()))
  print(multipleOf9(num[0]))
