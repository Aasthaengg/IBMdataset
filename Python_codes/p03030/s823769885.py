# 複数の値をキーにするソートを行うため、クラスを作成した。

# レストランを紹介する本のクラス。
class Book:
  	# インスタンス
    def __init__(self, no, name, value):
      	# レストラン番号(0から開始する)
        self.no = no
        # レストラン名
        self.name = name
        # レストラン評価
        self.value = value
# 本のクラスの配列。
book = []
n = int(input())
for i in range(n):
  	# レストラン名、レストラン評価
    s, p = input().split()
    book.append(Book(i, s, int(p)))

# レストラン評価の降順で整列する。
book = sorted(book, key=lambda b: b.value, reverse=True)
# レストラン名で整列する。
book = sorted(book, key=lambda b: b.name)
for b in book:
  	# 本に紹介されるレストラン順で表示する。
    print(b.no+1)
