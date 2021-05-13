def main():
    N = int(input())
    X = 1
    Y = 1
    Z = 1

    a = [0]*(N+1)

    for x in range(1,101,1):
        if x**2 + Y**2 + Z**2 + x*Y + Y*Z + Z*x > N:
            break
        for y in range(1,101,1):
            if x**2 + y**2 + Z**2 + x*y + y*Z + Z*x > N:
                break
            for z in range(1,101,1):
                if x**2 + y**2 + z**2 + x*y + y*z + z*x <= N:
                    a[x**2 + y**2 + z**2 + x*y + y*z + z*x] += 1
                elif x**2 + y**2 + z**2 + x*y + y*z + z*x > N:
                    break
    for i in range(1,N+1,1):
        print(a[i])

main()
