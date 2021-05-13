
if __name__ == '__main__':
    N = int(input())
    DIC = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    for _ in range(N):
        S = input()
        DIC[S] += 1

    for k, v in DIC.items():
        print(f'{k} x {v}')

