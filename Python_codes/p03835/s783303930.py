"""
int #整数
float #小数

#for
for name in fruits: #fruitの頭から操作
    print(name)
    
#リスト
list0 = [] #リスト生成
list0 = [1,2,3,4] #初期化
list0 = [0]*10 #[0,0,0,0,0,0,0,0,0,0]
list1= [i for i in range(10)] #>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = list(map(int, input().split()))　# 複数の入力をリストに入れる
number=[int(input()) for i in range(int(input()))] #複数行の入力をリストに
list1 = list1 + [6, 7, 8] #リストの追加
list2.append(34) #リストの追加　最後に（）内が足される
list.insert(3,10) #リストの追加　任意の位置（追加したい位置,追加したい値）
len(list4) #リストの要素数
max(sa) #list saの最小値
list5.count(2) #リスト(文字列も可）内の2の数
list1.sort() #並び替え小さい順
list1.sort(reverse=True)  #並び替え大きい順
set(list1) #list1内の重複している要素を削除し、小さい順に並べる
sum([2,3,   ,3]) #リストの合計

abs(a) #aの絶対値
max(a,b) min(a,b) #最大値　最小値
text1 = text1.replace("34","test") #text1内の"34"を"test"に書き換える(文字列内の文字を入れ替える)

exit(0) #強制終了
"""
K, S = map(int, input().split())
count = 0
for i in range(K + 1):
    for j in range(K + 1):
        Z=S-i-j
        if 0<=Z<=K:
            count += 1

print(count)
