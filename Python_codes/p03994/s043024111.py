import sys
from io import StringIO
import unittest
import os


# 実装を行う関数
def resolve():
    s = list(input())
    k = int(input())

    # 各桁をaにするために必要な処理回数を求める。(1桁ずつ求めていく)
    need_cnt_list = [26 - (ord(i) % 97) for i in s]
    # アルファベット(小文字)のaASCIIは97。なので、mod97でアルファベットを番号に置換できる(a=0 z=25)。ちなみに大文字Aは65。
    # for i in s:
    #     work += 26 - (ord(i) % 97)

    ans = []

    zan_cnt = k

    for num, i in enumerate(need_cnt_list):
        # 値がaの場合何もしない(既に最適解)
        if s[num] == "a":
            ans.append("a")
        # 値を1週させてaにできる場合、該当文字をaにする。
        elif zan_cnt >= i:
            zan_cnt -= i
            # 該当文字をaにする。
            ans.append("a")
        # 値を1週させてaにできない場合、その桁は何も処理せず次の桁に進む。
        else:
            ans.append(s[num])

    # 最後に、最終桁を延々と処理した結果が答え。
    # ※「余ったkを全て最終桁に使用した場合の最終桁の文字」で最終文字を置換
    now_last = ord(ans[-1]) - 97
    last = zan_cnt % 26 + now_last

    # 最終桁の文字を置き換え
    ans[-1] = chr(last + 97)
    print("".join(ans))
    return


# テストクラス
class TestClass(unittest.TestCase):
    def assertIO(self, assert_input, output):
        stdout, sat_in = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(assert_input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, sat_in
        self.assertEqual(out, output)

    def test_input_1(self):
        test_input = """xyz
4"""
        output = """aya"""
        self.assertIO(test_input, output)

    def test_input_2(self):
        test_input = """a
25"""
        output = """z"""
        self.assertIO(test_input, output)

    def test_input_3(self):
        test_input = """codefestival
100"""
        output = """aaaafeaaivap"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_1(self):
        test_input = """bbb
100000000"""
        output = """aaz"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_2(self):
        test_input = """bbb
75"""
        output = """aaa"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_2(self):
        test_input = """bbc
74"""
        output = """aaa"""
        self.assertIO(test_input, output)

    # 自作テストパターンのひな形(利用時は「tes_t」のアンダーバーを削除すること
    def test_1original_3(self):
            test_input = """bba
74"""
            output = """aay"""
            self.assertIO(test_input, output)


# 実装orテストの呼び出し
if __name__ == "__main__":
    if os.environ.get("USERNAME") is None:
        # AtCoder提出時の場合
        resolve()

    else:
        # 自PCの場合
        unittest.main()
