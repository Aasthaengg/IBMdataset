import collections
n = int(input())
v = list(map(int,input().split()))
a1 = []
a2 = []
for i in range(0,n,1):#スライスで絶対もっときれいにかけるなりねー
    if i%2==0:
        a1.append(v[i])
    if i%2==1:
        a2.append(v[i])

c1 = collections.Counter(a1)#配列を渡す
c2 = collections.Counter(a2)#配列を渡す
if c1.most_common()[0][0]!=c2.most_common()[0][0]:
    print(len(a1) - c1.most_common()[0][1] + len(a2) - c2.most_common()[0][1])#最も出現回数が多いものの出現回数
else:
    c12bannte = c1.most_common()[1][1] if len(c1)>1 else 0
    c22bannte = c2.most_common()[1][1] if len(c2)>1 else 0
    ans = min(len(a1) - c1.most_common()[0][1] + len(a2) - c22bannte,len(a1) - c12bannte + len(a2) - c2.most_common()[0][1])
    print(ans)