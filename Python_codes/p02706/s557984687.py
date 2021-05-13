def atc_163b(a: str, b: str) -> int:
    NM = a.split(" ")
    N = int(NM[0])
    M = int(NM[1])

    A = b.split(" ")
    A_int = [int(ai) for ai in A]
    play_days = N - sum(A_int)

    if play_days < 0:
        return -1
    else:
        return (play_days)

a = input()
b = input()

print(atc_163b(a, b))
