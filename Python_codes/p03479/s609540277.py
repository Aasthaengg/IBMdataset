#import collections
#aa = collections.Counter(a) # list to list
def readInts():
  return list(map(int,input().split()))
mod = 10**9 + 7
def main():
    x,y = readInts()
    now = x
    cnt = 0
    while now <= y:
        now *= 2
        cnt += 1
    print(cnt)



if __name__ == '__main__':
  main()
