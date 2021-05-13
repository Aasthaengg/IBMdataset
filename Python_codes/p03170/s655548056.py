if __name__ == "__main__":
    n,k = (int(x) for x in input().split())
    choice = [int(x) for x in input().split()]

    #print(n,k,choice)

    win = [False] * (k+1)
    for i in range(k+1):
        for x in choice:
            if i-x>=0 and not win[i-x]:
                win[i] = True
                break

    print("First" if win[k] else "Second")
