def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))

  
def main():
    n = int(input())
    a = sorted(Input())
    while len(a) > 1:
        x, y = a[0], a[1]
        a[0:2] = [(x+y)/2]
    return a[0]


print(main())