def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 単調増加になる区間の両端で売買
    actions = ['' for _ in range(N)]
    left = 0
    for right in range(1, N):
        if A[right - 1] > A[right]:
            if left != right - 1:
                actions[left] = 'buy'
                actions[right - 1] = 'sell'
            left = right
    if left != right:
        actions[left] = 'buy'
        actions[right] = 'sell'
    money = 1000
    stock = 0
    for i, action in enumerate(actions):
        if action == 'buy':
            stock = money // A[i]
            money -= stock * A[i]
        elif action == 'sell':
            money += stock * A[i]
            stock = 0
    print(money)


if __name__ == '__main__':
    main()
