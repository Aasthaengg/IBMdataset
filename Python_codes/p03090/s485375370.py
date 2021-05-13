def main():
    import itertools
    n = int(input())
    if n%2==0:
        rm = n+1
    else:
        rm = n
    ans = []
    for t in itertools.combinations((i+1 for i in range(n)), 2):
        if sum(t)!=rm:
            ans.append(t)
    print(len(ans))
    for a in ans:
        print(a[0],a[1])

if __name__ == "__main__":
    main()
