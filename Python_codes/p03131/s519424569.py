import math
k,a,b = map(int,input().split())

t = k
cnt = 1

#ビスケットと1円を交換したほうがいい時
if a+1<b:
    #1回1円と交換できるようになるまでビスケットを増やす
    cnt += a-1
    t -= a-1
    #print(cnt)
    #print(t)
    #ビスケットと1円を交換→1円とビスケットを交換を限界まで繰り返す
    cnt += b*math.floor(t/2)
    cnt -= a*math.floor(t/2)
    t -= 2 * math.floor(t/2)
    #print(cnt)
    #print(t)
    #ビスケットをたたいて増やす
    cnt += t
else:
    cnt +=k
print(cnt)