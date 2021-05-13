

def foo(xs, n):
    largest = - 10**6
    smallest = 10**6
    largest_i = -1
    smallest_i = -1
    for i, x in enumerate(xs):
        if largest < x:
            largest = x
            largest_i = i
        if smallest > x:
            smallest = x
            smallest_i = i

    ys = []
    if smallest < 0 and abs(smallest) > largest:
        for i in range(n-2, -1, -1):
            while xs[i+1] < xs[i]:
                xs[i] += smallest
                ys.append((smallest_i, i))
                if xs[i] < smallest:
                    smallest_i = i
                    smallest = xs[i]
    else:
        for i in range(1, n):
            while xs[i-1] > xs[i]:
                xs[i] += largest
                ys.append((largest_i, i))
                if xs[i] > largest:
                    largest_i = i
                    largest = xs[i]
    return ys



if __name__ == "__main__":
    n = int(input())
    xs = list(map(int, input().split()))
    ys = foo(xs, n)
    print(len(ys))
    for i, j in ys:
        print("%d %d"%(i+1, j+1))