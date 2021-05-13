from itertools import permutations, combinations_with_replacement

def calc(op, x, y):
    if op == "+":
        return x + y
    else:
        return x - y

def solve():
    A, B, C, D = map(int, list(input()))
    OP = combinations_with_replacement(["+", "-"], 3)
    for op in OP:
        O = permutations(op)
        s = set(O)
        for o in s:
            op1, op2, op3 = o
            tmp = calc(op3, calc(op2, calc(op1, A, B), C), D)
            if tmp == 7:
                print(f"{A}{op1}{B}{op2}{C}{op3}{D}=7")
                exit()

if __name__ == "__main__":
    solve()
