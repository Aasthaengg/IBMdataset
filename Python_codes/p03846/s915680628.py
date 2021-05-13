import math

def fail():
    print(0)
    exit()

def main():
    n = int(input())
    As = list(map(int, input().split(' ')))
    ind_lis = {}
    idx = n - 1
    while idx >= 0:
        ind_lis[idx] = 0
        idx -= 2
    for a in As:
        if a not in ind_lis:
            fail()
        ind_lis[a] += 1
        if a == 0 and ind_lis[a] > 1:
            fail()
        elif ind_lis[a] > 2:
            fail()
    print(2**(n//2)%(10**9 + 7))



if __name__ == '__main__':
    main()