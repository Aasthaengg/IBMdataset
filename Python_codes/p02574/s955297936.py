from math import gcd
n = int(input())
A = list(map(int, input().split()))
min_A = min(A)
max_A = max(A)

def is_pairwise():
    arr = [0] * (max_A + 1)
    for a in A:
        arr[a] += 1
    max_counter = 0
    for num in range(2, max_A + 1):
        counter = 0
        for i in range(1, 10**6 + 1):
            try:
                counter += arr[num * i]
            except:
                break
        max_counter = max(max_counter, counter)
    if max_counter == 1:
        return True
    else:
        return False

if min_A == 1 and max_A == 1:
    print("pairwise coprime")
elif min_A == 1 and max_A != 1:
    A = [num for num in A if num != 1]
    if is_pairwise():
        print("pairwise coprime")
    else:
        print("setwise coprime")
else:
    if is_pairwise():
        print("pairwise coprime")
    else:
        g = A[0]
        for a in A:
            g = gcd(a, g)
        if g == 1:
            print("setwise coprime")
        else:
            print("not coprime")