def main():

    A = input()
    n = len(A)
    ans = 1 + n*(n-1)//2 # +1 for unflipped case
    count = dict()
    for c in A:
        count[c] = count.get(c, 0) + 1
    for c in count:
        ans -= count[c] * (count[c] - 1) //2
    return ans

if __name__ == '__main__':
    print(main())