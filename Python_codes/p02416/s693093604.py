from sys import stdin
for line in stdin:
    if line == '0\n':
        break
    num = list(map(int, line.strip('\n')))
    print(sum(num))
