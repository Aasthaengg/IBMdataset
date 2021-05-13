def solve(s):
    return list(map(str.__eq__, list(s), list('CODEFESTIVAL2016'))).count(False)

if __name__ == '__main__':
    s = input()
    print(solve(s))