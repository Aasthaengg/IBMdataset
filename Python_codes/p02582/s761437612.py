from time import time
def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('temps écoulé', after - before)
        return rv
    return f


def A(S): 
    nb = 0
    if S == 'RSR':
        print(1)
        exit
    else:
        for i in S:
            if i == 'R':
                nb = nb+1
        print(nb)


@timer
def B():
    ...

@timer
def C():
    ...


S = input()
A(S)
