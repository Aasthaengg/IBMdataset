from pprint import pprint

s = str(input())


keyence_list = [[0,0] for _ in range(6)]

#下記のリストを埋めていく
#[[{keyenc},{e}],
# [{keyen},{ce}],
# [{keye},{nce}],
# [{key},{ence}],
# [{ke},{yence}],
# [{k},{eyence}]]


#前から探す
i = 0
if s[i] == "k":
    if s[i+1] == "e":
        if s[i+2] == "y":
            if s[i+3] == "e":
                if s[i+4] == "n":
                    if s[i+5] == "c":
                        if s[i+6] == "e":
                            print("YES")
                            exit()
                        else:
                            keyence_list[0][0] = 1
                    else:
                        keyence_list[1][0] = 1
                else:
                    keyence_list[2][0] = 1
            else:
                keyence_list[3][0] = 1
        else:
            keyence_list[4][0] = 1
    else:
        keyence_list[5][0] = 1
else:
    pass

#後ろから探す
j = len(s)-1
if s[j] == "e":
    if s[j-1] == "c":
        if s[j-2] == "n":
            if s[j-3] == "e":
                if s[j-4] == "y":
                    if s[j-5] == "e":
                        if s[j-6] == "k":
                            print("YES")
                            exit()
                        else:
                            keyence_list[5][1] = 1
                    else:
                        keyence_list[4][1] = 1
                else:
                    keyence_list[3][1] = 1
            else:
                keyence_list[2][1] = 1
        else:
            keyence_list[1][1] = 1
    else:
        keyence_list[0][1] = 1
else:
    pass

for k in range(6):
    for l in range(k,6):
        if keyence_list[k][0] == keyence_list[l][1] == 1:
            print("YES")
            exit()

print("NO")
exit()



#問題の読み違え
#一部分を削った文字列が"keyence"と一致しないといけない。（"keyence"を含む、ではない）
#from pprint import pprint
#
#s = str(input())
#
#keyence_list = [[float("inf"),-float("inf")] for _ in range(6)]
#
#
#
##前から探す
#for i in range(len(s)-6):
#    if s[i] == "k":
#        if s[i+1] == "e":
#            if s[i+2] == "y":
#                if s[i+3] == "e":
#                    if s[i+4] == "n":
#                        if s[i+5] == "c":
#                            if s[i+6] == "e":
#                                print("YES")
#                                exit()
#                            else:
#                                keyence_list[0][0] = min(keyence_list[0][0],i)
#                        else:
#                            keyence_list[1][0] = min(keyence_list[1][0],i)
#                    else:
#                        keyence_list[2][0] = min(keyence_list[2][0],i)
#                else:
#                    keyence_list[3][0] = min(keyence_list[3][0],i)
#            else:
#                keyence_list[4][0] = min(keyence_list[4][0],i)
#        else:
#            keyence_list[5][0] = min(keyence_list[5][0],i)
#    else:
#        pass
#
##後ろから探す
#for j in range(len(s)-1,5,-1):
#    if s[j] == "e":
#        if s[j-1] == "c":
#            if s[j-2] == "n":
#                if s[j-3] == "e":
#                    if s[j-4] == "y":
#                        if s[j-5] == "e":
#                            if s[j-6] == "k":
#                                print("YES")
#                                exit()
#                            else:
#                                keyence_list[5][1] = max(keyence_list[0][1],j-5)
#                        else:
#                            keyence_list[4][1] = max(keyence_list[1][1],j-4)
#                    else:
#                        keyence_list[3][1] = max(keyence_list[2][1],j-3)
#                else:
#                    keyence_list[2][1] = max(keyence_list[3][1],j-2)
#            else:
#                keyence_list[1][1] = max(keyence_list[4][1],j-1)
#        else:
#            keyence_list[0][1] = max(keyence_list[5][1],j)
#    else:
#        pass
#
##pprint(keyence_list)
#
#
#for k in range(6):
#    for l in range(k,6):
#        if keyence_list[k][0] <= keyence_list[l][1]:
#            print("YES")
#            exit()
#
#print("NO")
#exit()
#
#
#
#

#下記のリストを埋めていく
#[[{keyenc},{e}],
# [{keyen},{ce}],
# [{keye},{nce}],
# [{key},{ence}],
# [{ke},{yence}],
# [{k},{eyence}]]
#
# 0列目はsを前から走査し、1列目はsを後ろから走査
# 0列目のset{}の中で最小のものと、1列目のset{}の中で最大のものの大小関係がおかしくなければTrue
