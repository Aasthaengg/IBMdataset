import math
def main():
    N = int(input())
    t = 1
    l = []
    while len(l) < N:
        x = t * 10 + 1
        d = int(math.sqrt(x))
        for i in range(2, d+1):
            if x % i == 0:
                break
        else:
            l.append(x)
        t += 1
    print(' '.join(str(i) for i in l))
main()
