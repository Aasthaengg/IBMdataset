def answer(arr):
    n = len(arr)
    count = 0
    INC = 'INCREASING'
    DEC = 'DECREASING'
    STATE = None
    if n == 1 or n == 2:
        return 1
    for i in range(n-1):
        diff = arr[i+1] - arr[i]
        if diff == 0:
            continue
        if STATE is None:
            if diff > 0:
                STATE = INC
            if diff < 0:
                STATE = DEC
            count += 1
        elif STATE is INC:
            if diff < 0:
                STATE = None
        elif STATE is DEC:
            if diff > 0:
                STATE = None
        if STATE is None and i == n-2:
            count += 1
            
    return count

n = int(input())
arr = list(map(int, input().split()))
print(answer(arr))