from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    N,A,B = list(map(int,_in[0].split(' ')))  # type:list(int)
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    TF = 'Alice' if (B-A)%2==0 else 'Borys'
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(TF)
