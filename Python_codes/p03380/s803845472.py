def main():
  n = int(input())
  a = list(map(int, input().split()))
  a = sorted(a)
  a_i = a[-1]
  a_j = 0
  dist = a_i
  for i in range(len(a)-1):
    if abs(a_i/2-a[i]) < dist:
      a_j = a[i]
      dist = abs(a_i/2-a[i])
  print(a_i, a_j)

if __name__ == "__main__":
  main()