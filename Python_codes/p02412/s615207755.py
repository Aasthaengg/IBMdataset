import itertools as itr

def solve(n, x):
    return [sum(i) for i in itr.combinations(range(1, n+1), 3)].count(x)

if __name__ == '__main__':
    while True:
        n, x = [int(i) for i in input().split()]
        if n == x == 0: break
        print(solve(n, x))