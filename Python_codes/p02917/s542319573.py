def mapt(fn, *args):
    return tuple(map(fn, *args))

def Input():
    return mapt(int, input().split(" "))

def main():
    n = int(input())
    b = Input()
    data = 0
    for i in range(n-1):
        if i == 0:
            data += b[i]
            continue
        data += min(b[i], b[i-1])
    data += b[-1]
    print(data)
main()