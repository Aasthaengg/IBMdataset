def resolve():
    s = input()
    k = int(input())
    c = 0
    for i in range(k):
        if s[i] != "1":
            print(s[i])
            break
        if i == k-1:
            print(1)
resolve()