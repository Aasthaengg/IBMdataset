def c_time3_or_div2():
    N = int(input())
    A = [int(i) for i in input().split()]
    # a を 2 進数として下位ビットから見たとき，最初に 1 が現れるまでの 0 の個数
    return sum((a & -a).bit_length() - 1 for a in A)

print(c_time3_or_div2())