import sys
readline = sys.stdin.readline

def resolve():
    N = int(input())
    # A = input().replace(" ", "")
    # A = readline().rstrip().split()
    A = input().split()
    import collections
    counter = collections.Counter(A)
    if N % 2 == 1:
        if counter["0"] != 1:
            print("0")
            return
        for k, v in counter.items():
            if k == "0":
                continue
            if int(k) % 2 == 1:
                print("0")
                return
            if v != 2:
                print("0")
                return
    else:
        for k, v in counter.items():
            if int(k) % 2 == 0:
                print("0")
                return
            if v != 2:
                print("0")
                return
    
    print( (2**(N//2)) % (10**9+7) )




if '__main__' == __name__:
    resolve()

