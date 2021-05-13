def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    a = Input()
    sorted_a = sorted(a)
    point = max(a)//2
    center_index = len(a)//2
    right = sorted_a[center_index:]
    left = sorted_a[:center_index]
    print((point) - max(left) + min(right)-point)



main()