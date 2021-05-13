k,t = map(int,input().split())
a_input = list(map(int,input().split()))

#最も多いケーキをAtとする,a=4,b=1,c=1の場合を考えると
#a,b,a,c,a,aのようになる。よってa-(b+c)-1
max_a = max(a_input)
print(max(0,max_a-(k-max_a)-1))