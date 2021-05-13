N, A, B = map(int, raw_input() .split())
if N * A < B:
    print N * A
elif N * A > B:
    print B
else:
    print B
