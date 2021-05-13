if __name__ == "__main__":
    n = int(input().strip().split()[0])
    for i in range(n):
        data = list(map(int,input().strip().split()))
        c = max(data)
        data.remove(c)
        a,b = data
        if a **2 + b ** 2 == c**2 :print("YES")
        else:print("NO")