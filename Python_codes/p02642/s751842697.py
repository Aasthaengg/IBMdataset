def main():
  n = int(input())
  a = list(map(int, input().split()))

  ans = [0] * (max(a) + 1)
  length = max(a) + 1
  for x in a:
    if ans[x] == 0:
      for j in range(x, length, x):
        ans[j] += 1
    else:
      ans[x] += 1

  print(len(list(filter(lambda x: ans[x] == 1, a))))

  
if __name__ == '__main__':
  main()