def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    mon1 = [a for a in A]
    mon2 = [a for a in A]

    for i in range(10**9):
        mon1 = sorted(mon2)
        mon2 = list()

        for j in range(1, len(mon1)):
            m_ = mon1[j] % mon1[0]
            if m_ != 0:
                mon2.append(m_)

        mon2.append(mon1[0])

        if len(mon2) == 1:
            break

    print(mon2[0])
    
if __name__ == "__main__":
    main()