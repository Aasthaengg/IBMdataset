def main():
    k = int(input())
    hp = list(range(1, 10))
    for i in range(k-1):
        n = hp.pop(0)
        nm = n % 10
        val = n * 10 + nm
        
        if nm != 0:
            hp.append(val - 1)
        hp.append(val)
        if nm != 9:
            hp.append(val + 1)
    print(hp[0])

main()
