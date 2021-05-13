n = int(input())
kekw = input()

if n >= len(kekw):
    print(kekw)
elif n < len(kekw):
    kekwlist = list(kekw)
    for i in range(0, n):
        print(kekwlist[i], end = "")
    print("...")