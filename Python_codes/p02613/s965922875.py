if __name__ == "__main__":
    N = int(input())
    C0 = 0
    C1 = 0
    C2 = 0
    C3 = 0
    for i in range(N):
        S = input()
        if S == 'AC':
            C0 += 1
        elif S == 'WA':
            C1 += 1
        elif S == 'TLE':
            C2 += 1
        elif S == 'RE':
            C3 += 1

    print(f'AC x {C0}')
    print(f'WA x {C1}')
    print(f'TLE x {C2}')
    print(f'RE x {C3}')
