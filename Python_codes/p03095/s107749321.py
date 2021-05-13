#set(s)種類の文字で作れる文字列を考える
#s=abcab なら 
# 2個のaのどちらを使うか＋使わない => 3
# 2個のbのどれを使うか　＋　使わない => 3
# 1個のcを使うか　＋　使わない　=> 2
#3*3*2 からどれも使わない場合を覗くので3*3*2-1
from collections import Counter
n = int(input())
s = input()
a = Counter(s).values()
ans = 1
for i in a:
    ans *= i+1
print((ans-1)%1000000007)