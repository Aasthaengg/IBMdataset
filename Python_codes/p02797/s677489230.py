n,k,s = map(int,input().split())
#一旦s+1で全部埋める。
o = [s + 1] * n
#sがaの最大値の10^9の時はまずいので、1で埋めなおす
if(s == 10**9):o = [1] * n
#k個だけ、sで埋めなおす
for i in range(k):o[i] = s
#あとは出すだけ。
print(*o)