#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from itertools import combinations # (string,3) 3回
#from collections import deque
#import collections.defaultdict(list)
#import bisect
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    a,b,c,d,e,f = readInts()
    water = set()
    sugar = set()
    # water
    # A,B の制約が 1 <= A,B <= 30 だから、ループは31まで回せば位
    for i in range(31):
        for j in range(31):
            w = 100 * a * i + 100 * b * j
            if w <= f: # 水の合計が F より大きくなってはいけない (砂糖0gの時もあるが、)
            # -1g とかはないので
                water.add(w)
    # sugar
    # C,D の制約が、 1 <= C,D <= 3000 であるから、 3001 までまわせばい
    for i in range(3001):
        for j in range(3001):
            s = c * i  + d * j
            if s <= f: # 砂糖の合計が F より大きくなってはいけない
            # 水 0 g はあっても、-1gとかはないから
                sugar.add(s)
    # 濃度の限界値を決める
    nl = e/(100 + e) # *100 すれば、限界の濃度のパーセント
    noudo = -1
    ans1 = 0
    ans2 = 0
    for s in sugar:
        for w in water:
            # 砂糖水をつくる
            sum = s + w
            if sum == 0:# 和が0はだめー てか1 <= だから 1からループ回せばええやんけ
                continue
            x = s/sum # suger / 砂糖水 * 100 すれば%やで
            if sum <= f and x <= nl and x > noudo:
                # 砂糖水は fg以下 , 砂糖水の濃度は限界以下 , 濃度が最大になるまで回せ
                noudo = x
                ans1 = sum
                ans2 = s
    print(ans1,ans2)
if __name__ == '__main__':
  main()
