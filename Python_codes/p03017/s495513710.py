##agc034_a
N,A,B,C,D = map(int, input().split()) #A→C、B→D #4≤N≤200,000
S = [0] + list(input())

#すれ違うには . の3連続が必要
#すれ違わなくても、#が2連続であるとアウト

#すれ違いが必要かを判定する
#  A<B
#  A<C
#  B<D
#を利用すると下記の3パターンしかない。
if A < B < D < C:
    need_passing = True
elif (A < B < C < D) or (A < C < B < D):
    need_passing = False

#下記のように考える
#すれ違いが必要
    #Yes
        #すれ違い可能点(. . .)を列挙
        #A/B→すれ違い可能点へ行ける = 左記の区間に # # な並びがない
            #すれ違い可能点→C/Dへ行ける? = 左記の区間に # # な並びがない
    #No
        #A→CとB→Dで通行可能 = 左記の区間に # # な並びがない

passing_point_set = set() #すれ違い場所の始点のset
imos_stop = list() # "#"が2連続している場所で増加する。
imos_stop.append(0)

for i in range(1,N-1):
    if S[i] == S[i+1] == "#":
        imos_stop.append(imos_stop[-1] + 1)
    else:
        imos_stop.append(imos_stop[-1])

    if S[i] == S[i+1] == S[i+2] == ".":
        passing_point_set.add(i)

i = N-1
if S[i] == S[i+1] == "#":
    imos_stop.append(imos_stop[-1] + 1)
else:
    imos_stop.append(imos_stop[-1])
#i = N
#右側はない。
imos_stop.append(imos_stop[-1]) #   .##.

#print(imos_stop)
#print(passing_point_set)

def is_reachable(start,goal):
    if imos_stop[start] == imos_stop[goal] and start <= goal: #右に1か2マスにジャンプさせる ∴右方向にしか進めない
        return True
    else:
        return False

if need_passing == True: #A < B < D < C が成立している
    for passing_point in passing_point_set:
        if ((is_reachable(A,passing_point) == True and is_reachable(passing_point,C) == True and is_reachable(B,passing_point) == True and is_reachable(passing_point,D) == True and D != passing_point) or
            (B-1 in passing_point_set and is_reachable(A,C) == True and is_reachable(B,D) == True)):
            #passing pointの範囲内にDがある場合、passingできない場合がある
            #ex.   A#..D#  …これはOK。A#.BD#.  として、追い抜かせてからB→D
            #ex.   A#.D.# …これはOK。ただし、.D.がpassing_pointになる
            #ex.   A#D..#  …NG
                #↓のパターンが考察不足だった
                #  ##AB.#D..#C#  …start <= goal条件により、追い越し不可扱いになるが実際はできる
                #  ##A.B#D..#C#  …これはNG
                #  ##A.B#.D.#C#  …これはOK。.D.がpassing_pointになる
                #  ##A.B.#D..#C# …これはOK
            
            print("Yes")
            break
    else:
        print("No")
else:
    if is_reachable(A,C) == True and is_reachable(B,D) == True:
        print("Yes")
    else:
        print("No")
        
        
