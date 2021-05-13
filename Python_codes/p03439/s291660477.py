import sys

def solve():
    N = int(input())
    print("0" + "\n", flush = True)
    a = input()
    if a == "Vacant": return 0
    elif a == "Male": basis = 0
    else: basis = 1
    low, high = 0, N
    Fin = {0}
    while high - low > 1:
        mid = (low + high) // 2
        Fin |= {mid}
        print(str(mid) + "\n", flush = True)
        a = input()
        if a == "Vacant": break
        else:
            b = (0 if a == "Male" else 1)
            expected = (basis if mid % 2 == 0 else (basis + 1) % 2)
            if b != expected:
                high = mid
            else:
                low = mid
    else:
        if low in Fin: print(str(high) + "\n", flush = True)
        else: print(str(low) + "\n", flush = True)
        a = input()

    return 0

if __name__ == "__main__":
    solve()
