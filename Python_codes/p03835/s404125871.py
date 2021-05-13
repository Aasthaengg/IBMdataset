count = 0
if __name__ == "__main__":
    k, s = map(int, input().split())
    for i in range(k+1):
        for j in range(k+1):
            z = s - i - j
            if z >= 0 and  z <= k:
                count += 1 
    print(count)