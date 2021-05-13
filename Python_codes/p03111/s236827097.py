import abc
import itertools

def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    i = 0
    mps = []
    for assign in itertools.product([0, 1, 2, 3], repeat=N):
        if 1 not in assign or 2 not in assign or 3 not in assign:
            continue
        mp = 0
        abc_length = {1: 0, 2: 0, 3: 0}
        for i, abc in enumerate(assign):
            if abc == 0:
                continue
            elif abc_length[abc] == 0:
                abc_length[abc] = L[i]
            else:
                mp += 10
                abc_length[abc] += L[i]

        for key, goal in zip([1, 2, 3], [A, B, C]):
            mp += abs(goal - abc_length[key])
        mps.append(mp)
    print(min(mps))


if __name__ == '__main__':
    main()
