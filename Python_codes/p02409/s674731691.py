def main():
    for i in range(n):
        b, f, r, v = map(int, raw_input().split())
        x[b-1][f-1][r-1] += v
    for b in range(4):
        for f in range(3):
            print(' ' + ' '.join(map(str,x[b][f])))
        if b != 3:
            print('#'*20)
n = input()
x = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]
main()