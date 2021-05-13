from collections import Counter
N = int(input())
A = [int(i) for i in input().split()]
dic = Counter(A)
sticks = []
for i in dic:
    s = dic[i]
    if s>=4:
        sticks.append(i)
    if s>=2:
        sticks.append(i)
if len(sticks)<2:
    print(0)
else:
    sticks.sort(reverse=True)
    print(sticks[0]*sticks[1])