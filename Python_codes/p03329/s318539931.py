def main():
    from collections import deque
    N = int(input())

    amounts = [1]
    mul6 = 6
    while mul6 <= N:
        amounts.append(mul6)
        mul6 *= 6
    mul9 = 9
    while mul9 <= N:
        amounts.append(mul9)
        mul9 *= 9

    distances = [-1]*(N+1)
    distances[0] = 0

    targets = deque([0])
    while targets:
        t = targets.popleft()
        d = distances[t]
        for a in amounts:
            if t + a <= N and distances[t+a] == -1:
                distances[t+a] = d+1
                targets.append(t+a)
    print(distances[N])




main()