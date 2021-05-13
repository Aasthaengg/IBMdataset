'''
問題：
    あなたは AtCoder 王国の入国審査官です。
    入国者の書類にはいくつかの整数が書かれており、あなたの仕事はこれらが条件を満たすか判定することです。
    規約では、次の条件を満たすとき、またその時に限り、入国を承認することになっています。
        書類に書かれている整数のうち、偶数であるものは全て、3 または 5 で割り切れる。
    上の規約に従うとき、書類に N 個の整数 A1,A2,…,AN
    が書かれた入国者を承認するならば APPROVED を、しないならば DENIED を出力してください。
'''

'''
制約：
    入力はすべて整数
    1 ≤ N ≤ 100
    1 ≤ Ai ≤ 1000
'''
def is_even(num):  # 偶数判定
    if num % 2 == 0:
        return True
    else:
        return False

def is_fizzbuzz(num):  # 3 または 5で割り切れるか判定（※関数名はテキトーｗ）
    if num % 5 == 0:
        return True
    if num % 3 == 0:
        return True
    else:
        return False


# 標準入力から、N, A1,A2,...,AN の値を取得する
n = int(input())
numbers = list(map(int,input().split()))

result = 'APPROVED'
for i in numbers:
    if is_even(i):
        if is_fizzbuzz(i):
            result = 'APPROVED' # 偶数かつ、3でも5でも割り切れるので、APPROVED
        else:
            result = 'DENIED'   # 1つでも条件を満たさない場合、DENIEDしてfor文抜ける
            break

print(result)
