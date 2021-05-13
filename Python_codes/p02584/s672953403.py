
import glob
import os

bn = os.path.basename(__file__).split('.')[0]
dn = os.path.dirname(__file__).split('/')

# 問題ごとのディレクトリのトップからの相対パス
REL_PATH = dn[len(dn)-2] + '\\' + dn[len(dn)-1] + '\\' + bn

# テスト用ファイル置き場のトップ
TOP_PATH = 'C:\\AtCoder'

class Common:

    problem = []
    index = 0

    def __init__(self, rel_path):
        self.rel_path = rel_path

    def initialize(self, path):
        file = open(path)
        self.problem = file.readlines()
        self.index = 0
        return

    def input_data(self):
        try:
            IS_TEST
            self.index += 1
            return self.problem[self.index-1]

        except NameError:
            return input()

    def resolve(self):
        pass

    def exec_resolve(self):
        try:
            IS_TEST
            for path in glob.glob(TOP_PATH + '\\' + self.rel_path + '/*.txt'):
                print("Test: " + path)
                self.initialize(path)
                self.resolve()
                print("\n\n")
        except NameError:
            self.resolve()


class Solver(Common):

    def resolve(self):

        X, K, D = map(int, self.input_data().split())
        if abs(X) > K * D:
            result = abs(X) - K * D
        else:
            if int(abs(X) / D) % 2 == K % 2:
                result = abs(X) - int(abs(X) / D) * D
            else:
                result = (int(abs(X) / D) + 1) * D - abs(X)

        print(str(result))


solver = Solver(REL_PATH)
solver.exec_resolve()
