def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    counter = {}
    for num in A:
        counter[num] = counter.get(num, 0) + 1
    for i in range(1, N+1):
        print(counter.get(i, 0))

if __name__ == "__main__":
    solve()