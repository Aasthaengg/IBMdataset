from itertools import accumulate

def chk(samp):
    for i in samp:
        print(samp)

N,W = map(int,input().split())

w = [0 for i in range(N)]
v = [0 for i in range(N)]

for i in range(N):
    w[i],v[i]=map(int,input().split())



#価値毎に置き換える
wl = [[] for i in range(4)]

#価値ごとのりすとに入れていく
for i in range(N):
    wl[w[i]-w[0]].append(v[i])


#ソートして最初に0を追加する。0は選択しない場合
for i in range(4):
    wl[i].sort(reverse = 1)
    wl[i].insert(0,0)
    

#累積和を作る
for i in range(4):
    wl[i] = list(accumulate(wl[i]))
    
#出力用変数
out = 0


for i,wl0 in enumerate(wl[0]):
   for j,wl1 in enumerate(wl[1]):
       for k,wl2 in enumerate(wl[2]):
           for l,wl3 in enumerate(wl[3]):
               if i*(w[0])+j*(w[0]+1)+k*(w[0]+2)+l*(w[0]+3) > W:
                   pass
               else:
                   out = max(out,wl0+wl1+wl2+wl3)
                   
print(out)