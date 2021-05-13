
while True:
    z = list(map(str, input()))
    if "-" in z:
        break
    n = int(input())
    for i in range(n):
        a=int(input())
        z=z[a:]+z[:a]
    print("".join(z))