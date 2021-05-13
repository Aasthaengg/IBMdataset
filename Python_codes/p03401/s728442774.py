#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n = int(input())
    A = [0] + readInts() + [0]
    S = 0
    for i in range(1,n+2):
        S += abs(A[i] - A[i-1])
    #print(S)
    for i in range(1,n+1):
        print(S + abs(A[i-1] - A[i+1]) - (abs(A[i-1] - A[i]) + abs(A[i] - A[i+1])))
    


if __name__ == '__main__':
  main()
