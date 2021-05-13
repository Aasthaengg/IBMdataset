from sys import stdin


if __name__ == "__main__":
    _in = [_.rstrip() for _ in stdin.readlines()]
    s =     _in[0]   # type:str
    # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    _s = s[0]+str(len(s[1:-1]))+s[-1]
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    print(_s)
