def main():
    A, B = map(int, input().split())
    s, t, a, b = '.', '#', A, B
    if A > B:
        s, t, a, b = t, s, b, a
    S = 100
    T = [[s] * S for _ in range(S)]
    
    a -= 1
    for i in range(b):
        X, Y = (i * 4)// len(T) * 4, ((i * 4)% len(T))
        T[X][Y:Y+3] = [t] * 3
        T[X+1][Y:Y+3] = [t] * 3
        T[X+2][Y:Y+3] = [t] * 3
        if a > 0:
            T[X+1][Y+1] = s
            a -= 1
    print(len(T), len(T[0]))
    for t in T:
        print(''.join(t))
main()
