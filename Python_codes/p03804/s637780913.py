n,m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(input())
for j in range(m):
    b.append(input())

# 考え：同じ文字列の並びがあるか各行、各列で見る
# 方針：画像の左上から各行ごとに先頭からAとBの文字列を比較していきマッチするかどうかを調べる

"""ボツ案
a_pix = []
b_pix = []
a_temp = []
b_temp = []

judge = ''

for i in a:
    for i_pix in i:
        a_temp.append(i_pix)
    a_pix.append(a_temp)
    a_temp = []

for j in b:
    for j_pix in j:
        b_temp.append(j_pix)
    b_pix.append(b_temp)
    b_temp = []

# print(a_pix)
# print(b_pix)
"""

for i in range(n-m+1):
    for j in range(n-m+1):


        judge = 'Yes'
        for k in range(m):
            for l in range(m):
                # 横にずらして文字列を比較
                if a[i+k][j+l] != b[k][l]:
                    judge = 'No'

        if judge == 'Yes':
            print('Yes')
            exit()

print('No')