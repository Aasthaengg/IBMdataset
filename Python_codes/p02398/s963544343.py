def spliter():
    a, b, c = map(int, input().split())
    return a, b, c

def count(a, b, c):
    count = 0
    for i in range(a, b + 1):
        if c % i == 0:count +=1
    return count

def main():
    a, b, c = spliter()
    print(count(a, b, c))

if __name__ == '__main__':
    main()