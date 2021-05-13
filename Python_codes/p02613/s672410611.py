def main():

    d = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    N = int(input())
    for _ in range(N):
        S = input()
        d[S] += 1

    for s in ['AC', 'WA', 'TLE', 'RE']:
        print(s + ' x ' + str(d[s]))

if __name__ == '__main__':
    main()
