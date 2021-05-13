def resolve():
    N, M = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())), reverse=True)
    total = sum(A)
    choose = 0
    th = total/(4*M)
    for a in A:
        if a < th:
            continue
        choose += 1
    print("Yes" if choose >= M else "No")



if '__main__' == __name__:
    resolve()