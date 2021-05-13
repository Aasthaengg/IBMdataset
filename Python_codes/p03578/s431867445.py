from collections import Counter
import sys

N = int(input())
D = list(map(int, input().split()))
D = sorted(D)
D_counter = Counter(D)


M = int(input())
T = list(map(int, input().split()))
T = sorted(T)
T_counter = Counter(T)



D_keylist = (list(D_counter.items()))

T_keylist = (list(T_counter.keys()))
T_Valuelist = (list(T_counter.values()))


ans = 0
T_index = 0

for i in D_keylist:
    D_key = i[0] # N個の問題案の中のi個めの問題案の番号
    D_value = i[1] # N個の問題案の中のi個めの問題案の難易度

    T_key = T_keylist[T_index] # M個の問題案の中のi個めの問題案の番号
    T_value = T_Valuelist[T_index] # M個の問題案の中のi個めの問題案の番号


    if D_key == T_key and (D_value >= T_value): #もしNとMの番号問題が一致しており、なおかつN個の問題の方が難易度が多かったら加算
        T_index = T_index + 1 #もし一致していたら、Mの問題番号を横にひとつずらす
        ans = ans + 1 #加算

        if T_index == M:
            break
    else:
        pass


if len(T_keylist) == ans: #M個の問題を作る事ができればYES,無理ならNO
    print("YES")
else:
    print("NO")