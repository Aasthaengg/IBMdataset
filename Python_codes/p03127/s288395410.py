#ABC 118 C - Monsters Battle Royale 21:58

def func(A):
    #(1)Aの最小値mを見つける
    #(2)Aの要素をmで割った余りで配列A'を作る（０は無視）
    #A'の要素が０個の場合、mが答え
    A = sorted(A)
    m = min(A)
    B = [A[0]]
    
    for i in range(1,len(A)):
        if A[i]%m != 0:
            B.append(A[i]%m)
    
    if len(B) == 1:
        print(m)
        return len(B)
    else:
        func(B)
    
n = int(input())
A = list(map(int, input().split()))
func(A)