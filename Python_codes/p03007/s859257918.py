def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a = list(sorted(a))
    min_a = a.pop(0)
    max_a = a.pop(-1)

    pos_a = filter(lambda x: x >= 0, a)
    neg_a = filter(lambda x: x < 0, a)
    procedure = []
    
    state = min_a
    for _a in pos_a:
        procedure.append((state, _a))
        state -= _a

    procedure.append((max_a, state))
    state = max_a - state

    for _a in neg_a:
        procedure.append((state, _a))
        state -= _a

    print(state)
    for t in procedure:
        print(t[0], t[1])

if __name__ == "__main__":
    solve()