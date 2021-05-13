a, b, h = map(int, open(0).read().split())

def Trapezoids(a, b, h):
    return (a + b) * h // 2

if __name__ == '__main__':
    print(Trapezoids(a, b, h))