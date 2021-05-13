def resolve():
    N = int(input())
    T, A = list(map(int, input().split()))
    H = list(map(int, input().split()))
    temp = [abs(T - x * 0.006 - A) for x in H]
    print(temp.index(min(temp))+1)

    return

resolve()