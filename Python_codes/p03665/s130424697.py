N, P = map(int, input().split())
Alist = list(map(int, input().split()))
guuki = [A%2 for A in Alist]
odd = guuki.count(1)
even = guuki.count(0)
if odd == 0:
    if P == 0:
        print(2**N)
    else:
        print(0)
else:
    print(2**(N-1))