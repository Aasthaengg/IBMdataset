n = int(input())
v = list(map(int,input().split()))
from collections import Counter
even = Counter(v[::2]).most_common(2)
odd = Counter(v[1::2]).most_common(2)
even.append((0,0))
odd.append((0,0))
youso = n//2
if even[0][0] == odd[0][0]: # 一緒だったら、差が小さい方を優先するのです?
    print(min(youso - even[1][1] + youso - odd[0][1],youso - odd[1][1] + youso - even[0][1]))
else: # 違うやつなら、それに合わせよう
    print(youso - even[0][1] + youso - odd[0][1])
