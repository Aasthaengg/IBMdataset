import sys
from io import StringIO
import unittest
import os
from collections import deque

# 再帰処理上限(dfs作成時に設定するのが面倒なので限度近い値を組み込む)
sys.setrecursionlimit(999999999)


# 実装を行う関数
def resolve(test_def_name=""):
    que = deque()
    que.extend(list(input()))
    q = int(input())
    query_s = [list(input().split()) for i in range(q)]

    isReverse = False
    for query in query_s:
        if query[0] == "1":
            isReverse = True if not isReverse else False
        else:
            # 先頭に追加
            if (isReverse is False and query[1] == "1") or (isReverse and query[1] == "2"):
                que.appendleft(query[2])
            # 末尾に追加
            else:
                que.append(query[2])

    ans = ""
    if isReverse:
        ans = "".join(list(reversed(que)))
    else:
        ans = "".join(que)

    print(ans.replace("\r", ""))


# パターン
# !isReverse 1(先頭)　= 先頭に追加
#  isReverse 1(先頭)　= 末尾に追加
# !isReverse 2(末尾)　= 先頭に追加
#  isReverse 2(末尾)　= 先頭に追加

# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve(sys._getframe().f_back.f_code.co_name)
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def tes_t_1original_1(self):
        test_input = """データ"""
        output = """データ"""
        self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
