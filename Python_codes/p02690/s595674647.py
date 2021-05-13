import glob
import bisect

# 問題ごとのディレクトリのトップからの相対パス
REL_PATH = 'ABC\\166\\D'

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

    def calc(self, num):
        if num < 2:
            return 0
        return num * (num-1) / 2

    def resolve(self):

        X = int(self.input_data())

        squares = [0]*401
        for i in range(0,401):
            squares[i] = (i-200) ** 5

        finish = False
        for i in range (1,401):
            for j in range(0,400):
                if squares[i] - squares[j] == X:
                    print(str(i-200) + ' ' + str(j-200))
                    finish = True
                    break
            if finish:
                break


solver = Solver(REL_PATH)
solver.exec_resolve()
