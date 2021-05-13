from itertools import groupby

s1=input()
k=int(input())

s2=[[h, len(list(g))] for h, g in groupby(s1)] #…(*)

c=0
if len(s2)!=1:
    #接合していない部分の数え上げ
    for i in range(len(s2)):
        #i==0またはlen(s2)-1は接合部なので一旦数えない
        if i!=0 and i!=len(s2)-1:
            c+=(s2[i][1]//2)*k
    #接合部が同じ文字でできているかどうか数え上げの仕方が変わる
    if s2[0][0]==s2[-1][0]:
        c+=((s2[0][1]+s2[-1][1])//2)*(k-1)
        c+=(s2[0][1]//2+s2[-1][1]//2)
    else:
        c+=(s2[0][1]//2+s2[-1][1]//2)*k

else:
    #len(s2)=1の場合は全て同じ文字の文字列になる
    c+=(s2[0][1]*k)//2

print(c)

'''
配列について前から順に要素をまとめていく関数
def groupby(a):
    a2=[[a[0],1]]
    for i in range(1,len(a)):
        if a2[-1][0]==a[i]:
            a2[-1][1]+=1
        else:
            a2.append([a[i],1])
    return a2
s2=groupby(s1)


from itertools import groupby
# チーム番号が割り振られたメンバーリスト
# {'team': チーム番号, 'name': 名前}
members = [{'team': 1, 'name': 'A'},
           {'team': 3, 'name': 'B'},
           {'team': 2, 'name': 'C'},
           {'team': 1, 'name': 'D'},
           {'team': 2, 'name': 'E'}]
# groupbyを使うには、まずはグルーピングしたいキーでソートする必要がある
members.sort(key=lambda m: m['team'])
# チーム番号でグルーピング
for key, group in groupby(members, key=lambda m: m['team']):
    print("key:", key) # キーとして指定したチーム番号を出力
    for member in group:
        print(member) # 同じキー（チーム番号）のメンバーを出力
$ python3 groupby.py
key: 1
{'team': 1, 'name': 'A'}
{'team': 1, 'name': 'D'}
key: 2
{'team': 2, 'name': 'C'}
{'team': 2, 'name': 'E'}
key: 3
{'team': 3, 'name': 'B'}
'''