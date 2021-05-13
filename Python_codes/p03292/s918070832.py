def main():
    A, B, C = map(int, input().split())
    costs = [A, B, C]
    costs.sort()
    print((costs[1] - costs[0]) + (costs[2] - costs[1]))
main()