from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    S =     _in[0]   # type:str
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    s = '2018'+S[4:]
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(s)
