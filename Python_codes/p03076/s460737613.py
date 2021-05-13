def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    l = [A, B, C, D, E]
    c = []
    for i in range(len(l)):
        if i == 0:
            c.append(l[i])
        else:
            if c[0] % 10 > l[i] % 10 and l[i] % 10 != 0:
                c.insert(0, l[i])
            else:
                c.append(l[i])
    ans = 0
    for i in range(len(c)):
        if i == 0:
            ans += c[i]
        else:
            if c[i] % 10 != 0:
                t = c[i] % 10
                ans = ans + c[i] + (10 - t)
            else:
                ans = ans + c[i]
    print(ans)        
main()