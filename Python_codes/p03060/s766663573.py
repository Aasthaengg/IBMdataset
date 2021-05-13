def main():
    n = int(input())
    gems = [int(x) for x in input().split()]
    cost = [int(x) for x in input().split()]
    res = []
    for i in range(n):
        res.append(gems[i] - cost[i])
    soma_n = sum([x if x > 0 else 0 for x in res])
    print(soma_n)
main()