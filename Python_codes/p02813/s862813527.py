from itertools import permutations


def mapt(fn, *args):
    return tuple(map(fn, *args))
  

def main():
    n = int(input())
    data = permutations(range(1, n+1), n)
    p = mapt(int, input().split(" "))
    q = mapt(int, input().split(" "))

    list1 = []
    for index, i in enumerate(data):
        if p == i or i == q:
            list1.append(index)
    print(abs(list1[0] - list1[-1]))
main()