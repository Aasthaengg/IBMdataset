import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

S = read().rstrip().decode()

is_YYMM = 1 <= int(S[2:]) <= 12
is_MMYY = 1 <= int(S[:2]) <= 12

if is_YYMM and is_MMYY:
    print('AMBIGUOUS')
elif is_YYMM:
    print('YYMM')
elif is_MMYY:
    print('MMYY')
else:
    print('NA')