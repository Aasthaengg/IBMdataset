# -*- coding: utf-8 -*-

#k回対戦済

S = input()

#リストに変換
S_list = []
for i in range(0,len(S)):
    S_list.append(S[i])
#print(S_list)

#勝ち数
Nvic = S_list.count("o")

if Nvic + 15 - len(S) < 8:
    print("NO")
else:
    print("YES")
