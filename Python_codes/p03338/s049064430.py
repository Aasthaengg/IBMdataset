
if __name__ == '__main__':
    n =int(input())
    s=input()
    max =0
    for i in range(n):
        a= set(s[:i])
        b= set(s[i:])
        count = len(a &b)
        if max <count:
            max=count

    print(max)