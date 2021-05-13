from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N,A,B = list(map(int,_in[0].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    while True:
        if A+1 != B:
            A += 1
        else:
            TF = 'Borys'
            break
        if B-1 != A:
            B -= 1
        else:
            TF = 'Alice'
            break
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(TF)
