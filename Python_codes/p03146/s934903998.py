def main():
    s = int(input())
    e = set([s])
    i = 1
    while True:
        i += 1
        s = f(s)
        if s in e:
            print(i)
            return
        e.add(s)
    
def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1
    
if __name__ == "__main__":
    main()