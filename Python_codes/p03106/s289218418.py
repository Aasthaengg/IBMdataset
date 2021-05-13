"""
全探索
1からmin(a,b)の中でaとbを割り切るものの数をカウントする
"""
a, b, k = map(int, input().split())
counter = 0
for i in list(range(1,min(a,b)+1))[::-1] :
    if a%i == 0 and b%i == 0 :
        counter += 1
    if counter == k :
        print(i)
        break
