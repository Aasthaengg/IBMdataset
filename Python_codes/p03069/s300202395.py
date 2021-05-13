def solve(s):
    n = len(s)
    count_white_right = [0]*(n+1)
    count_black_left = [0]*(n+1)
    for i in range(n):
        count_black_left[i+1] = count_black_left[i] + (1 if s[i]=='#' else 0)
    for i in range(n)[::-1]:
        count_white_right[i] = count_white_right[i+1] + (1 if s[i]=='.' else 0)
    return min([count_black_left[i] + count_white_right[i] for i in range(n+1)])


def main():
    _ = int(input())
    s = input()
    print(solve(s))

if __name__ == "__main__":
    main()

import unittest
class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solve('#.#'), 1)
    def test2(self):
        self.assertEqual(solve('#.##.'), 2)
    def test3(self):
        self.assertEqual(solve('.........'), 0)
    def test4(self):
        self.assertEqual(solve('#'), 0)
    def test5(self):
        self.assertEqual(solve('.'), 0)
    def test6(self):
        self.assertEqual(solve('#.'), 1)
    def test7(self):
        self.assertEqual(solve('##'), 0)
    def test8(self):
        self.assertEqual(solve('..'), 0)
    def test9(self):
        self.assertEqual(solve('.#'), 0)
    def test10(self):
        self.assertEqual(solve('#'*1000 + '.' * 999), 999)
    def test11(self):
        self.assertEqual(solve('#'*999 + '.' * 1000), 999)
