#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    s = input()
    k = int(input())
    #LIST = {s}
    #for i in range(k):
    #    for j in range(len(s) - i):
    #        LIST.add(s[j:j+i+1])
    #print(LIST)
    #print(sorted(list(LIST))[k-1])
    # 辞書順で5番目、長さは最長でも5
    r = []
    for i in range(1,6): # 1 ~ 5 文字のながさ 1から5文字まで
        for j in range(len(s) - i + 1): # 見る範囲 len(s) - j  ~ len(s) - j + i まで最後まで見てる!
            r.append(s[j:j+i])
    #print(r)
    print(sorted((set(r)))[k-1])


if __name__ == '__main__':
  main()
