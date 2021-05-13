h, w = list(map(int, input().split()))
A = [['#'] * (w + 2)] + [list('#' + input() + '#') for _ in range(h)] + [['#'] * (w + 2)]
[print(''.join(a)) for a in A]