def abc134c():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    a_sorted = sorted(a)
    for item in a:
        if item == a_sorted[-1]:
            print(a_sorted[-2])
        else:
            print(a_sorted[-1])
abc134c()