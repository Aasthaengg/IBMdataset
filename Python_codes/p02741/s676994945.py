
import glob


# 問題ごとのディレクトリのトップからの相対パス
REL_PATH = 'ABC\\159\\A'

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

        tmp = "1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51"
        data = tmp.split(",")

        N = int(self.input_data())

        print(str(data[N-1]))



solver = Solver(REL_PATH)
solver.exec_resolve()
