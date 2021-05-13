# coding: utf-8
def main():
    n, k = map(int, input().split())
    if n == k:
        return 0
    elif n < k:
        tmp = abs(n - k)
        if tmp < n:
            return tmp
        else:
            return n
    else:
        tmp = n // k
        n -= k * tmp
        tmp = abs(n - k)
        if tmp < n:
            return tmp
        else:
            return n
            
    
print(main())
