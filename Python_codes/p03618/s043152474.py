#editorial参照
#答えは(i < jかつAi̸=Ajであるような組(i; j)の個数) +1
#上記のi～jの反転はi+1～j-1の反転と同等
#回文や接尾辞とかの厄介なアルゴリズムは不要
a = input()
n = len(a)
chrs = set(a)
dic = {k:0 for k in chrs}

for i in range(n):
    dic[a[i]] += 1

ans = n*(n-1)//2+1

for k in dic:
    ans -= dic[k]*(dic[k]-1)//2

print(ans)