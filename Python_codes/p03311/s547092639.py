import statistics

if __name__ == "__main__":
    N = int(input())
    A = [float(x) for x in input().split(" ")]
    A = [a - i - 1 for i, a in enumerate(A)]
    med = statistics.median(A)
    A = [abs(a - med) for a in A]
    print(int(sum(A)))
