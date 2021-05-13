import math

if __name__ == '__main__':
    n =int(input())
    a = int(math.sqrt(n))

    max=1
    for i in range(2,a+1):
        now = i*i
        while now <= n:
            if max < now:
                max =now
            now = now*i
    print(max)