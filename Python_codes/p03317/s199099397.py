#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n,k = readInts()
    A = readInts()
    import math
    nokori = n - k
    #print(nokori)
    cnt = 1
    cnt += math.ceil(nokori/(k-1))
    print(cnt)




if __name__ == '__main__':
  main()
