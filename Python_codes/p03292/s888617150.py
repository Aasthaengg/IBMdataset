def ABC_103_A():
    A1,A2,A3 = map(int, input().split())

    cost1 = 0 + abs(A2-A3) + abs(A3-A1)
    cost2 = 0 + abs(A2-A1) + abs(A3-A2)
    cost3 = abs(A1-A2) + 0 + abs(A3-A1)
    cost4 = abs(A1-A3) + 0 + abs(A3-A2)
    cost5 = abs(A1-A3) + abs(A2-A1) + 0
    cost6 = abs(A1-A2) + abs(A2-A3) + 0

    print(min(cost1,cost2,cost3,cost4,cost5,cost6))

if __name__ == '__main__':

    ABC_103_A()