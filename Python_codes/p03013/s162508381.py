import sys

sys.setrecursionlimit(1000000)

MOD = 1000000007

state = [-1 for i in range(100010)]

def step_state(n, broken):
    if state[n] != -1:
        return state[n]

    if n == 0:
        state[0]=1
        return 1
    elif n == 1:
        if broken[1]:
            state[1]=0
            return 0
        else:
            state[1]=1
            return 1
    else:
        if broken[n - 1] and broken[n - 2]:
            state[n]=0
            return 0
        elif broken[n - 1]:
            state[n]=step_state(n-2, broken) % MOD
            return state[n]
        elif broken[n-2]:
            state[n] = step_state(n-1, broken) % MOD
            return state[n]
        else:
            state[n] = (step_state(n-1, broken)+step_state(n-2, broken)) % MOD
            return state[n]


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = set([int(input()) for i in range(m)])
    broken = [False] * (n+1)
    for i in range(n+1):
        if i in a:
            broken[i] = True

    answer = step_state(n, broken)

    print(answer)
