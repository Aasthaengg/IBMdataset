import sys
def main():
  k, t = map(int, input().split())
  a = list(map(int, input().split()))
  if t == 1:
    print(a[0]-1)
    sys.exit()
  a.sort(reverse = True)
  key = [0, 1]
  num = 0
  while True:
    k = num%2
    a[key[k]]-=1
    sub = 0
    if a[key[k]] == 0:
      key[k] = max(key) + 1
      if key[k] < t:
        if a[key[0]] >= a[key[1]]:k=0
        else:k = 1
        num = k-1
      else:
        sub = 1
        break
    num += 1
  print(sum(a)-sub)
  
if __name__ == "__main__":
  main()