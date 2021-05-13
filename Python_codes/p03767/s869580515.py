n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
# 上位 2/3を取得
aa=a[:2*n]
# 上位から1,2..1,2 と割り振る場合の2位の集合を取得
aaa=aa[1::2]

print(sum(aaa))